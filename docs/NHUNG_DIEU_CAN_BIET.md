# Những Điều Cần Biết Trước Khi Thực Hành (Prerequisites)

Tài liệu này liệt kê những kiến thức, phần cứng và phần mềm bạn cần chuẩn bị để chạy thành công dự án nhận diện cử chỉ tay trên NVIDIA Jetson.

## 1. Kiến thức nền tảng
Bạn không cần phải là chuyên gia AI, nhưng nên nắm vững các kiến thức cơ bản sau:
- **Python cơ bản**: Biết cách viết script, chạy file `.py`, cài đặt thư viện (`pip install`).
- **Command Line (Terminal)**: Biết các lệnh cơ bản (`cd`, `ls`, `mkdir`, `sudo`) vì chúng ta sẽ thao tác nhiều trên terminal của Linux (Ubuntu trên Jetson).
- **Khái niệm cơ bản về Computer Vision**: Hiểu cơ bản về ảnh số (pixel, RGB), Webcam là gì và FPS (Frames Per Second).

## 2. Yêu cầu Phần cứng
Dự án này được tối ưu cho các thiết bị biên (Edge Devices), cụ thể:
- **Máy tính nhúng**: NVIDIA Jetson Nano, Jetson TX2, Xavier NX, hoặc Orin (Nano/AGX).
  - *Lưu ý*: Code vẫn có thể chạy trên Laptop/PC Windows hoặc MacBook bình thường (dùng Webcam tích hợp).
- **Webcam**: Bất kỳ USB Webcam nào (Logitech C270, C920...) hoặc Camera CSI (Raspberry Pi Camera V2 - cần cấu hình thêm).
- **Phụ kiện**:
  - Nguồn điện ổn định cho Jetson (tối thiểu 5V/4A cho Nano).
  - Quạt tản nhiệt (rất quan trọng khi chạy AI liên tục).

## 3. Yêu cầu Phần mềm & Môi trường
Đây là phần các bạn mới thường gặp rắc rối nhất do sự xung đột phiên bản.

### Hệ điều hành
- **Jetson**: Ubuntu 18.04 (JetZooPack 4.6) hoặc Ubuntu 20.04 (JetPack 5.x/6.x).
- **PC**: Windows 10/11, macOS, hoặc Linux.

### Thư viện Python (Dependencies)
File `requirements.txt` đã liệt kê các thư viện cần thiết. Tuy nhiên, hãy lưu ý đặc biệt các điểm sau:

1. **Python Version**: Nên dùng **Python 3.8** trở lên.
   - *Trên Jetson Nano cũ (Ubuntu 18.04)*: Mặc định là Python 3.6. Bạn CẦN cài thêm Python 3.8 hoặc 3.9 để chạy được phiên bản MediaPipe mới nhất.

2. **MediaPipe**:
   - Đây là "bộ não" của dự án.
   - Thư viện này xử lý việc tìm các điểm khớp tay.
   - **Phiên bản khuyến nghị**: `mediapipe==0.10.14`.

3. **Numpy**:
   - **QUAN TRỌNG**: MediaPipe hiện tại (đến giữa 2024/2025) thường gặp lỗi với `numpy` phiên bản 2.0 trở lên.
   - **Bắt buộc**: Phải cài `numpy<2.0.0` (ví dụ 1.26.x). Nếu không code sẽ báo lỗi rất khó hiểu khi import.

4. **OpenCV**:
   - Dùng để đọc camera và vẽ hình.
   - Trên Jetson, nên ưu tiên dùng bản OpenCV được cài sẵn theo JetPack (thường là 4.1.1 hoặc 4.5.x) để tận dụng tăng tốc phần cứng. Nếu cài qua pip (`opencv-python`), nó là bản chạy bằng CPU, sẽ chậm hơn một chút nhưng dễ cài đặt hơn.

## 4. Các bước thực hành gợi ý
1. **Đọc README**: Hiểu dự án làm gì.
2. **Đọc Deployment Guide**: Nếu bạn dùng Jetson, hãy đọc kỹ file `docs/deployment_guide.md` để biết cách cài môi trường đặc thù.
3. **Cài đặt**: Chạy `pip install -r requirements.txt`.
4. **Chạy thử**: Chạy `python src/hand_gesture.py` và đưa tay vào trước camera.

## 5. Xử lý sự cố thường gặp
- **Lỗi `ModuleNotFoundError`**: Quên chưa `pip install`.
- **Lỗi Camera đen ngòm**: Camera đang bị process khác chiếm dụng, hoặc bạn chọn sai ID (thử sửa 0 thành 1 trong code).
- **Lỗi `AttributeError: module 'numpy' has no attribute...`**: Do bạn đang dùng Numpy 2.0. Hãy chạy `pip install "numpy<2.0"` để fix.

---
---

## 6. Lộ trình "Thực hành" khi chưa có Jetson
Đây là câu hỏi rất thực tế. Nếu chưa có bo mạch, bạn không thể test hiệu năng thực tế, NHƯNG bạn có thể luyện tập các kỹ năng cốt lõi để **khi có máy là chạy được ngay**:

1.  **Luyện Linux (Quan trọng nhất)**:
    - Jetson chạy Ubuntu. Mọi thao tác đều qua dòng lệnh.
    - **Hành động ngay**: Đọc [Hướng Dẫn Thực Hành WSL](HUONG_DAN_WSL.md) để bắt đầu cài đặt môi trường Ubuntu ngay trên Windows của bạn.

2.  **Kiểm thử Logic (Logic Testing)**:
    - Chạy code trên PC (Windows/Linux) để đảm bảo Camera hoạt động, nhận diện đúng ngón tay.
    - Mục đích: Đảm bảo phần mềm "sạch" lỗi trước khi đưa sang môi trường khó tính như Jetson.

3.  **Docker & Cross-Compilation (Nâng cao)**:
    - Nếu bạn muốn thử thách, hãy tìm hiểu về **Docker buildx** để build một image docker cho ARM64 ngay trên máy tính x86 của bạn. Đây là kỹ năng "Senior" của kỹ sư Edge AI.

---
*Chúc bạn thực hành vui vẻ!*
