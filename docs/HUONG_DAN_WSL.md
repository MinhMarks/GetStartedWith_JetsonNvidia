# Hướng Dẫn Thực Hành trên WSL (Windows Subsystem for Linux)

Thực hành trên WSL là cách tuyệt vời để bạn làm quen với môi trường dòng lệnh Linux (Ubuntu) giống hệt như trên NVIDIA Jetson, mà không cần mua thiết bị.

## 1. Mở Terminal WSL
Từ Start Menu của Windows, gõ "Ubuntu" hoặc "WSL" và mở cửa sổ Terminal lên. Bạn sẽ thấy màn hình đen với dòng lệnh chờ.

## 2. Cài đặt các gói hệ thống (System Dependencies)
Đây là bước **quan trọng nhất** để mô phỏng Jetson. Trên Windows bạn cài file `.exe`, nhưng trên Linux bạn dùng `apt-get`.

Chạy lần lượt các lệnh sau (nhập mật khẩu của bạn khi được hỏi):

```bash
# 1. Cập nhật danh sách gói phần mềm
sudo apt-get update

# 2. Cài đặt Python và PIP (nếu chưa có)
sudo apt-get install -y python3 python3-pip

# 3. Cài đặt các thư viện bổ trợ cho OpenCV (Rất quan trọng!)
# Nếu thiếu cái này, OpenCV sẽ báo lỗi "ImportError: libGL.so.1..."
sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
```

## 3. Tải Code và Cài đặt thư viện Python

```bash
# 1. Clone code về (như bình thường)
git clone https://github.com/your-username/JetsonHandGesture.git
cd JetsonHandGesture

# 2. (Khuyên dùng) Tạo môi trường ảo để không ảnh hưởng hệ thống
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate

# 3. Cài đặt thư viện của dự án
pip install -r requirements.txt
```

## 4. Chạy ứng dụng & Vấn đề Camera trên WSL

### Thử chạy
```bash
python3 src/hand_gesture.py
```

### ⚠️ Lưu ý về Webcam trên WSL
Mặc định, WSL **không thể nhìn thấy** Webcam của Laptop bạn (vì lý do bảo mật của Windows).
- **Trường hợp 1 (Đơn giản)**: Chương trình chạy lên, in ra "Đang mở Camera..." rồi báo lỗi không tìm thấy Camera và thoát.
    - -> **Chúc mừng!** Bạn đã cài đặt môi trường thành công. Code đã chạy đúng logic. Việc không mở được Camera là do hạn chế của WSL, không phải do bạn làm sai.

- **Trường hợp 2 (Muốn Camera chạy thật)**:
    - Bạn cần cài đặt công cụ **USBIPD-WIN** trên Windows để "chia sẻ" Webcam vào trong WSL.
    - Đây là kỹ thuật nâng cao. Nếu bạn muốn thử, hãy tìm từ khóa: *"Connect USB devices to WSL using USBIPD"*.

### Cách test thay thế (Không cần USBIPD)
Bạn có thể sửa code `src/hand_gesture.py` một chút để đọc từ **File Video** thay vì Webcam (`0`).
1. Quay một video ngắn bàn tay của bạn (`test.mp4`), copy vào thư mục dự án.
2. Sửa dòng `cap = cv2.VideoCapture(0)` thành `cap = cv2.VideoCapture('test.mp4')`.
3. Chạy lại code -> Bạn sẽ thấy AI nhận diện trên video!

---
*Chúc mừng bạn đã làm chủ được dòng lệnh Linux!*
