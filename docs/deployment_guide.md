# Hướng dẫn Deploy lên NVIDIA Jetson 

Tài liệu này hướng dẫn bạn cách đưa file `hand_gesture.py` lên chạy trên bo mạch NVIDIA Jetson (Nano / TX2 / Xavier / Orin).

## 1. Chuẩn bị Phần cứng
- **NVIDIA Jetson** đã được cài image hệ điều hành (JetPack).
- **USB Webcam** (Kết nối vào cổng USB của Jetson).
- Màn hình + Chuột + Phím (để thao tác trực tiếp) HOẶC Laptop kết nối qua SSH.

## 2. Cài đặt Môi trường trên Jetson

Jetson chạy kiến trúc **ARM64 (aarch64)**, không phải x86_64 như PC thông thường, nên việc cài đặt thư viện đôi khi cần lưu ý phiên bản.

**Bước 1: Cập nhật hệ thống**
Mở Terminal trên Jetson và chạy:
```bash
sudo apt-get update
sudo apt-get upgrade
```

**Bước 2: Cài đặt pip và các thư viện cơ bản**
```bash
sudo apt-get install python3-pip
pip3 install --upgrade pip
```

**Bước 3: Cài đặt OpenCV**
Thường JetPack đã cài sẵn OpenCV. Kiểm tra bằng lệnh:
```bash
python3 -c "import cv2; print(cv2.__version__)"
```
Nếu chưa có hoặc lỗi, có thể cài lại: `sudo apt-get install python3-opencv`

**Bước 4: Cài đặt MediaPipe**
Đây là phần quan trọng nhất. 
*Cách dễ nhất (cho các bản JetPack mới và Python 3.8+):*
```bash
pip3 install mediapipe
```
*Nếu gặp lỗi không tìm thấy phiên bản phù hợp (đặc biệt trên Jetson Nano cũ chạy Python 3.6):*
Bạn cần tải file `.whl` do cộng đồng build sẵn hoặc tự build.
- **Link tải file whl phổ biến:** [JetsonHacks - Install MediaPipe](https://github.com/jetsonhacks/jetson-inference) (Google search "mediapipe for jetson nano aarch64").
- Ví dụ lệnh cài từ file whl: `pip3 install mediapipe-0.8.x-cp36-cp36m-linux_aarch64.whl`

## 3. Chạy ứng dụng

**Bước 1: Copy code**
Copy file `hand_gesture.py` vào Jetson (dùng USB hoặc dùng lệnh `scp` từ máy tính).

**Bước 2: Kết nối Webcam**
Cắm Webcam vào. Kiểm tra xem nó là thiết bị nào (thường là `/dev/video0`):
```bash
ls /dev/video*
```
Nếu bạn có nhiều camera, bạn có thể cần sửa dòng `cv2.VideoCapture(0)` trong code thành `1` hoặc `2`.

**Bước 3: Chạy code**
```bash
python3 hand_gesture.py
```

## 4. Tối ưu hóa (Tips cho Jetson)

Các thiết bị Jetson (như Nano) có tài nguyên giới hạn. Để chạy mượt hơn:

1. **Giảm độ phân giải Camera:**
   Thêm vào code trước vòng lặp:
   ```python
   cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
   ```

2. **Dùng model "nhẹ" (Lite):**
   Trong code `hand_gesture.py`, tham số `model_complexity=0` đã được tôi set sẵn. Đây là chế độ Lite chạy nhanh nhất. Nếu muốn chính xác hơn (và chạy chậm hơn), hãy đổi thành `1`.

3. **Chế độ Max Power (Nên bật):**
   Trên Jetson, hãy bật chế độ hiệu năng cao nhất:
   ```bash
   sudo nvpmodel -m 0
   sudo jetson_clocks
   ```

## 5. Xử lý lỗi thường gặp

- **Lỗi `GStreamer warning`**: Thường do OpenCV không giao tiếp tốt với Camera. -> Thử cài lại `opencv-python-headless` hoặc kiểm tra lại kết nối Camera.
- **Lỗi `ImportError`**: Do chưa cài đủ thư viện (numpy, mediapipe). Hãy pip install lại cái thiếu.
- **Chậm / Latency cao**: Giảm độ phân giải hoặc tắt cửa sổ hiển thị (`cv2.imshow`) nếu không cần thiết (chạy headless).
