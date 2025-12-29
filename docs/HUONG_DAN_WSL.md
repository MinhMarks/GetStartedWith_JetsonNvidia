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

# 3. Cài đặt các thư viện bổ trợ cho OpenCV
# Lưu ý: Trên Ubuntu mới (22.04/24.04), gói 'libgl1-mesa-glx' đã đổi tên.
sudo apt-get install -y libgl1 libglib2.0-0
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

### ⚠️ Vấn đề: WSL không thấy Camera
Mặc định, WSL bị "cô lập" nên không thấy Webcam của Laptop. Bạn có 2 cách giải quyết:

---

### Cách 1: Dùng File Video (Dễ nhất - Khuyên dùng)
Thay vì vật lộn với driver, bạn hãy quay 1 video ngắn bàn tay (`test.mp4`), copy vào thư mục code và chạy:

1. Copy video vào thư mục đang đứng.
2. Sửa code `src/hand_gesture.py`:
   ```python
   # Tìm dòng này:
   cap = cv2.VideoCapture(0)
   # Sửa thành:
   cap = cv2.VideoCapture('test.mp4') 
   ```
3. Chạy lại `python3 src/hand_gesture.py`. Nếu nó hiện video và nhận diện tay -> **Thành công 100% về mặt code**.

---

### Cách 2: "Mount" Camera thật vào WSL (Nâng cao)
Nếu bạn nhất quyết muốn dùng Webcam thật (livestream), bạn cần công cụ **USBIPD-WIN**.

**B1: Trên Windows (PowerShell Administrator)**
1. Cài đặt: `winget install usbipd`
2. Cắm Webcam (hoặc nếu là camera laptop thì bỏ qua).
3. Liệt kê thiết bị: `usbipd list`
   - Tìm dòng có chữ "Integrated Webcam" hoặc "USB Video Device". Nhớ cái **BUSID** (ví dụ: `2-4`).
4. Chia sẻ thiết bị: `usbipd bind --busid <BUSID_CUA_BAN>`
5. Gắn vào WSL: `usbipd attach --wsl --busid <BUSID_CUA_BAN>`

**B2: Trong WSL (Terminal Ubuntu)**
1. Cài driver:
   ```bash
   sudo apt-get install linux-tools-virtual hwdata
   sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/*/usbip 20
   ```
2. Kiểm tra lại: `ls /dev/video*`
   - Nếu thấy `/dev/video0` hiện ra là thành công!

---

---
*Chúc mừng bạn đã làm chủ được dòng lệnh Linux!*
