# 🚀 Jetson Hand Gesture: AI Trên Thiết Bị Biên

![Banner](https://img.shields.io/badge/AI-Computer%20Vision-blueviolet?style=for-the-badge) 
![Platform](https://img.shields.io/badge/Platform-Jetson%20%7C%20PC%20%7C%20WSL-success?style=for-the-badge)
![Library](https://img.shields.io/badge/Powered%20By-MediaPipe-orange?style=for-the-badge)

> **"Mang khả năng nhìn của AI vào thiết bị nhỏ gọn."**

Chào mừng bạn đến với dự án **Jetson Hand Gesture**! Đây là nơi bạn sẽ học cách xây dựng một hệ thống nhận diện cử chỉ tay thời gian thực, tối ưu hóa để chạy mượt mà trên các thiết bị nhúng như NVIDIA Jetson Nano/Orin( Hoặc giả lập môi trường Linux trên Windows).

## ✨ Bạn Sẽ Làm Được Gì?
Chỉ với một chiếc Camera, hệ thống này có thể:
- 👋 **Hello**: Nhận diện bàn tay mở.
- ✊ **Fist**: Nhận diện nắm đấm.
- ✌️ **Victory**: Nhận diện ngón tay chữ V.
- ☝️ **Pointer**: Điều khiển ảo bằng ngón trỏ.

⚡ **Tốc độ**: >30 FPS trên Laptop và ~20 FPS trên Jetson Nano (với cấu hình tối ưu).

---

## 🛠️ Bạn Cần Chuẩn Bị Gì?

### Phần cứng
- **Lý tưởng nhất**: Một bộ NVIDIA Jetson (Nano, TX2, Orin...).
- **Đừng lo nếu không có**: Máy tính cá nhân (Windows/Linux/Mac) là đủ để học!

### Phần mềm
- Python 3.8+
- Webcam (hoặc file video quay sẵn).

📚 **Tài liệu quan trọng cho người mới:**
- [Những Điều Cần Biết Trước Khi Bắt Đầu](docs/NHUNG_DIEU_CAN_BIET.md) (Rất nên đọc!)
- [Hướng Dẫn Cài Đặt trên PC](docs/CHAY_TREN_PC.md)

---

## 🚫 Không Có Thiết Bị Jetson? Đừng Lo!
Mục đích của dự án này là giúp bạn hiểu về **Quy trình AI Biên (Edge AI Workflow)**. Bạn hoàn toàn có thể luyện tập các kỹ năng "triệu đô" ngay trên máy tính của mình:

### 1. Giả lập môi trường Linux (WSL)
Jetson chạy Linux Ubuntu. Hãy biến Windows của bạn thành Linux bằng WSL.
👉 **Thực hành ngay**: [Hướng Dẫn Chi Tiết WSL & Sửa Lỗi Camera](docs/HUONG_DAN_WSL.md)

### 2. Test Logic với File Video
Bạn không cần camera xịn để code AI. Hãy quay một video tay của bạn, và viết code để xử lý video đó.
- Nếu code chạy ngon trên video -> Nó sẽ chạy ngon trên Jetson.

### 3. Tối ưu hóa Code
Thử thách: Làm sao để code chạy nhanh hơn?
- Giảm độ phân giải khung hình?
- Dùng model `Lite` thay vì `Full`?
- Đây là tư duy của một kỹ sư Edge AI thực thụ!

---

## 🚀 Bắt Đầu Nhanh (Quick Start)

### 1. Cài đặt
```bash
git clone https://github.com/your-username/JetsonHandGesture.git
cd JetsonHandGesture
pip install -r requirements.txt
```

### 2. Chạy thử
```bash
python src/hand_gesture.py
```
*(Nhấn **'q'** để thoát)*

---

## 📂 Cấu trúc dự án
- `src/`: Mã nguồn chính.
- `docs/`: Tài liệu hướng dẫn chi tiết (Tiếng Việt).
- `requirements.txt`: Các thư viện cần thiết.

---
*Dự án được xây dựng để hỗ trợ cộng đồng yêu thích AI & IoT.*
