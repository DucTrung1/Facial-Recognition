# Ứng dụng Nhận Diện Khuôn Mặt 

## Mục Tiêu và Mục Đích
Ứng dụng này được phát triển để nhận diện khuôn mặt và mắt trong một hình ảnh. Nó cung cấp một công cụ hữu ích cho các ứng dụng liên quan đến nhận diện khuôn mặt.

## Tính Năng Chính và Chức Năng
- Nhận diện khuôn mặt trong hình ảnh.
- Vẽ hình chữ nhật xung quanh khuôn mặt đã tìm thấy.
- Sử dụng nhiều bộ phát hiện mắt khác nhau.
## Các bước ứng dụng nhận diện khuôn mặt
Dưới đây là các bước cụ thể để ứng dụng đoạn mã nhận diện khuôn mặt và mắt sử dụng OpenCV:
- Bước 1: Chuẩn bị môi trường:
Đảm bảo bạn đã cài đặt OpenCV và các thư viện liên quan trong môi trường Python của bạn.
- Bước 2: Chuẩn bị ảnh và tệp XML:
Đặt ảnh bạn muốn xử lý vào đúng đường dẫn (image_path).
Tải xuống tệp XML cho bộ phát hiện khuôn mặt và mắt hoặc sử dụng các tệp XML mẫu từ OpenCV.
- Bước 3: Cấu hình tham số:
Điều chỉnh các thông số như scale_factor, min_neighbors, và min_size tùy thuộc vào nhu cầu của bạn.
- Bước 4: Gọi hàm detect_faces_and_eyes:
Gọi hàm detect_faces_and_eyes với các tham số đã thiết lập và hình ảnh đầu vào.
Hàm này sẽ thực hiện nhận diện khuôn mặt và mắt và vẽ hình chữ nhật xung quanh chúng.
- Bước 5: Chạy chương trình:
Chạy chương trình Python của bạn và kiểm tra kết quả được hiển thị trong cửa sổ "Khuôn mặt phát hiện".
- Bước 6: Kiểm tra và điều chỉnh:
Quan sát kết quả và kiểm tra số lượng khuôn mặt đã nhận diện.
Nếu cần thiết, điều chỉnh các tham số để đạt được kết quả tốt hơn.
- Bước 7: Tích hợp vào ứng dụng lớn hơn (nếu cần):
Nếu bạn muốn tích hợp đoạn mã vào một ứng dụng lớn hơn, bạn có thể sử dụng hàm detect_faces_and_eyes trong phần xử lý ảnh của ứng dụng của bạn.


## Cách Sử Dụng
1. Clone dự án từ GitHub về máy của bạn:
2. Thay đổi đường dẫn phù hợp với máy tính của bạn
![image](https://github.com/DucTrung1/Facial-recognition/assets/148746928/f33403ef-d929-4d9d-9e7e-e68589d3938e)
## Hướng Dẫn Sử Dụng Ứng Dụng

1. **Chọn Hình Ảnh**: Mở file `app.py` và đặt đường dẫn của hình ảnh bạn muốn sử dụng:

    ```python
    image_path = 'C:\\Users\\ductr\\FacialRecognition\\imgs\\hinh1.jpg'
    và
    eye_cascade_paths = [
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_eye.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_righteye.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_eye_tree_eyeglasses.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_lefteye_2splits.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_eyepair_big.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_leftear.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_lefteye.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_mouth.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_mcs_upperbody.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_profileface.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_smile.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\lbpcascade_frontalface.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\lbpcascade_profileface.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\lbpcascade_silverware.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_russian_plate_number.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_lowerbody.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\lbpcascade_frontalface_improved.xml',
    'C:\\Users\\ductr\\FacialRecognition\\imgs\\lbpcascade_frontalcatface.xml'
]

    ```

2. **Điều Chỉnh Thông Số (Tùy Chọn)**:
- Nếu cần, bạn có thể điều chỉnh các thông số như `new_scale_factor`, tùy thuộc theo độ sáng, tối của hình ảnh.

    ```python
    new_scale_factor = 1.1
    new_min_neighbors = 3
    new_min_size = (40, 40)
    ```

3. **Chạy Ứng Dụng**:
  - Sau khi đã điều chỉnh các thông số, chạy ứng dụng bằng cách thực hiện lệnh sau trong terminal:

    ```bash
    python app.py
    ```

4. **Kiểm Tra Kết Quả**:
- Kết quả nhận diện khuôn mặt sẽ được hiển thị trong cửa sổ đồ họa, bằng việc vẽ hình vuông xung quanh khuôn mặt và đếm số khuôn mặt

