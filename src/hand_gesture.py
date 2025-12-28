import cv2
import mediapipe as mp
import time

# Khởi tạo MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Cấu hình model
hands = mp_hands.Hands(
    model_complexity=0, # 0 để chạy nhanh (nhẹ), phù hợp cho Jetson Nano
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=2 # Nhận diện tối đa 2 tay
)

def count_fingers(hand_landmarks):
    """
    Đếm số ngón tay đang giơ lên dựa trên tọa độ landmark.
    Logic đơn giản: So sánh vị trí đầu ngón tay (TIP) với khớp nối (PIP/MCP).
    """
    fingers = []
    
    # Landmark IDs cho các đầu ngón tay
    # Thumb: 4, Index: 8, Middle: 12, Ring: 16, Pinky: 20
    
    # 1. Ngón cái (Thumb) - Logic hơi khác các ngón còn lại
    # Kiểm tra xem đầu ngón cái (4) có nằm bên trái/phải khớp (3) hay không (tùy tay trái/phải)
    # Tuy nhiên để đơn giản cho demo này: so sánh tọa độ x
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1) # Coi như đang mở (lưu ý: logic này phụ thuộc chiều tay, demo đơn giản)
    else:
        fingers.append(0)

    # 2. 4 ngón còn lại (Index, Middle, Ring, Pinky)
    # So sánh tọa độ y của đầu ngón (TIP) và khớp nối (PIP - khớp giữa)
    # Lưu ý: Trong ảnh, trục y hướng xuống dưới (giá trị càng cao càng ở dưới)
    # Nên nếu y_tip < y_pip nghĩa là ngón đang giơ lên cao.
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)
            
    return fingers

def get_gesture_name(fingers):
    """
    Đặt tên cử chỉ dựa trên danh sách trạng thái ngón tay (e.g., [1,1,1,1,1])
    """
    # fingers[0] là ngón cái. Lưu ý logic ngón cái ở trên chỉ là tương đối.
    # Ta chủ yếu dựa vào 4 ngón còn lại cho chính xác hơn trong demo đơn giản.
    
    count = sum(fingers)
    
    # Logic đơn giản hóa (bỏ qua ngón cái để tránh nhiễu khi xoay tay)
    four_fingers = fingers[1:] 
    count_4 = sum(four_fingers)
    
    if count_4 == 4:
        return "Hi / Open Hand" # Xòe cả bàn
    elif count_4 == 0:
        return "Fist / Closed" # Nắm đấm
    elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
        return "Peace / Victory" # Giơ ngón trỏ và giữa
    elif fingers[1] == 1 and count_4 == 1:
        return "One / Pointing" # Chỉ tay
    else:
        return "Unknown"

print("-> Đang mở Camera... Nhấn 'q' để thoát.")
cap = cv2.VideoCapture(0) # Camera index 0

if not cap.isOpened():
    print("Lỗi: Không thể mở Camera.")
    exit()

prev_frame_time = 0
new_frame_time = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Bỏ qua frame trống.")
        continue

    # 1. Chuẩn bị ảnh
    # MediaPipe cần RGB, OpenCV đọc là BGR
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 2. Inference (Chạy model)
    results = hands.process(image)

    # 3. Vẽ kết quả
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Vẽ khung xương tay
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            
            # Xử lý Logic nhận diện
            fingers = count_fingers(hand_landmarks)
            gesture = get_gesture_name(fingers)
            
            # Hiển thị tên cử chỉ ngay cạnh tay (lấy tọa độ cổ tay làm gốc)
            wrist_x = int(hand_landmarks.landmark[0].x * image.shape[1])
            wrist_y = int(hand_landmarks.landmark[0].y * image.shape[0])
            
            cv2.putText(image, gesture, (wrist_x, wrist_y - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Tính FPS
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Hiển thị
    cv2.imshow('Jetson Hand Gesture Demo', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
