import cv2

def detect_faces_and_eyes(image_path, face_cascade_path, eye_cascade_paths, scale_factor=1.1, min_neighbors=5, min_size=(30, 30)):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=min_size)

    total_faces = len(faces)  # Tạo một biến để đếm tổng số khuôn mặt

    if total_faces > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            for eye_cascade_path in eye_cascade_paths:
                eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
                roi_gray = gray_image[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=min_size)

                # Tại đây, bạn có thể thực hiện các tác vụ khác với vị trí của mắt nếu cần

    # In ra số lượng khuôn mặt và mắt đã tìm thấy
    print(f"Số lượng khuôn mặt: {total_faces}")
    

    # Tạo cửa sổ có thể điều chỉnh kích thước và hiển thị hình ảnh
    cv2.namedWindow('Khuôn mặt phát hiện', cv2.WINDOW_NORMAL)
    cv2.imshow('Khuôn mặt phát hiện', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đường dẫn của hình ảnh mà bạn muốn sử dụng
image_path = 'C:\\Users\\ductr\\FacialRecognition\\imgs\\hinh1.jpg'
# Đường dẫn của tệp XML cho bộ phát hiện khuôn mặt
face_cascade_path = 'C:\\Users\\ductr\\FacialRecognition\\imgs\\haarcascade_frontalface_default.xml'
# Đường dẫn của tệp XML cho bộ phát hiện mắt
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

# Điều chỉnh các thông số:
new_scale_factor = 1.1
new_min_neighbors = 3
new_min_size = (40, 40)

# Gọi hàm với các thông số mới
detect_faces_and_eyes(image_path, face_cascade_path, eye_cascade_paths, scale_factor=new_scale_factor, min_neighbors=new_min_neighbors, min_size=new_min_size)

    

