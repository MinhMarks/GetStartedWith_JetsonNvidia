# Lộ trình Phát triển AI trên Thiết bị Edge (NVIDIA Jetson)

Chào mừng bạn bước vào thế giới **Edge AI** (AI biên)! Có lẽ thiết bị bạn nhắc đến là **NVIDIA Jetson** (Nano / Orin / v.v.), một dòng máy tính nhỏ gọn nhưng mạnh mẽ chuyên dùng để chạy AI.

Tài liệu này sẽ hướng dẫn bạn từ con số 0 đến khi có thể tự deploy (triển khai) một mô hình AI lên thiết bị.

## Giai đoạn 1: Chuẩn bị Kiến thức Nền tảng (Software)

Trước khi chạm vào phần cứng, bạn cần nắm vững quy trình tạo ra một "bộ não" AI trên máy tính thường (PC/Laptop).

### 1.1 Python & Thư viện cơ bản
Bạn đang đi đúng hướng với `torch_vs_numpy.py` trong workspace hiện tại!
- **Numpy**: Xử lý mảng, ma trận.
- **PyTorch / TensorFlow**: Hai thư viện chính để tạo và train mô hình AI.
    - *Khuyên dùng:* **PyTorch** hiện nay rất phổ biến và dễ học.
- **OpenCV**: Thư viện xử lý ảnh (đọc webcam, resize ảnh, vẽ khung nhận diện).

### 1.2 "Hello World" của AI
Đừng bắt đầu quá phức tạp. Hãy chạy thử các bài toán kinh điển:
1. **Image Classification (Phân loại ảnh):** Đưa vào ảnh con chó -> máy trả về "Dog".
2. **Object Detection (Phát hiện vật thể):** Đưa video vào -> máy vẽ khung quanh người, xe cộ (YOLO model là vua ở mảng này).

---

## Giai đoạn 2: Phần cứng (Hardware - "The Jackson")

"Jackson" mà bạn nghe có thể là **Jetson Nano**, **Jetson Orin Nano**, hoặc **Jetson AGX Orin**.

### 2.1 Mua gì?
- **NVIDIA Jetson Nano (cũ)**: Rẻ, đủ để học cơ bản.
- **NVIDIA Jetson Orin Nano (mới)**: Mạnh hơn nhiều, hỗ trợ AI hiện đại tốt hơn.

### 2.2 Cài đặt (Setup)
Khi có thiết bị, bạn không cài Windows. Bạn sẽ cài **JetPack SDK** (dựa trên Linux Ubuntu).
- **Hệ điều hành:** Linux (Ubuntu). Bạn nên làm quen các lệnh Terminal cơ bản (`ls`, `cd`, `sudo`, `apt-get`).
- **Phần mềm:** JetPack sẽ cài sẵn CUDA, TensorRT, OpenCV cho bạn.

---

## Giai đoạn 3: Quy trình Triển khai (Workflow)

Đây là bức tranh toàn cảnh cách bạn đưa AI từ máy tính xuống thiết bị:

1. **Training (Trên PC/Cloud):**
   - Dùng GPU mạnh trên PC để dạy mô hình học (Train).
   - Kết quả: File mô hình (ví dụ: `model.pth` của PyTorch hoặc `model.onnx`).

2. **Optimization (Tối ưu hóa):** *Đây là bước quan trọng cho thiết bị yếu*
   - Thiết bị Edge không mạnh như PC, nên cần "nén" mô hình lại.
   - **TensorRT**: Công cụ "thần thánh" của NVIDIA giúp mô hình chạy siêu nhanh trên Jetson.
   - **TVM** (MiniTVM trong thư mục của bạn là ví dụ về hướng này): Một trình biên dịch AI giúp chạy model trên nhiều loại phần cứng khác nhau.

3. **Inference (Chạy thực tế trên Jetson):**
   - Chép file mô hình đã tối ưu vào Jetson.
   - Viết code Python/C++ để đọc Camera -> Chạy Model -> Điều khiển Robot/Hiển thị.

---

## Tài liệu & Khóa học Khuyên dùng

### Miễn phí & Chính chủ (Tốt nhất)
1. **Jetson AI Fundamentals (NVIDIA):** 
   - Khóa học "vỡ lòng" cực hay. Dạy làm máy phân loại rác, robot tránh vật cản.
   - Link: [NVIDIA Deep Learning Institute](https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs)
2. **JetsonHacks (YouTube/Blog):** Kênh hướng dẫn thực chiến số 1 về Jetson.
3. **Dusty-nv / jetson-inference:**
   - Một kho code mẫu (Repo GitHub) huyền thoại. Chỉ cần tải về là chạy được nhận diện vật thể ngay lập tức.
   - Link: [GitHub - dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference)

---

## Bước tiếp theo cho bạn

1. **Xác nhận thiết bị:** Hãy kiểm tra xem bạn định mua hay đã có thiết bị tên chính xác là gì?
2. **Thực hành ngay trên PC:** Bạn không cần đợi có Jetson mới học được. Hãy thử chạy code nhận diện vật thể (YOLOv8) ngay trên máy tính Windows của bạn để hiểu input/output hoạt động thế nào.
