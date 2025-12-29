import cv2

def check_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"[-] Camera {index}: Không thể mở.")
        return False
    
    ret, frame = cap.read()
    if ret:
        print(f"[+] Camera {index}: Hoạt động TỐT! (Resolution: {frame.shape[1]}x{frame.shape[0]})")
        cap.release()
        return True
    else:
        print(f"[-] Camera {index}: Mở được nhưng không đọc được hình (Black screen).")
        cap.release()
        return False

print("--- Kiểm tra Camera ---")
# Thử index 0, 1, 2
for i in range(3):
    print(f"Đang kiểm tra index {i}...")
    check_camera(i)
print("-----------------------")
print("Hãy dùng index nào có dấu '[+]' để sửa vào file hand_gesture.py")
