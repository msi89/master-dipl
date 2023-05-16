# Импорт необходимые библиотеки
import cv2
import numpy as np

# Загрузка каскада классификаторов для обнаружения лиц
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Загрузка каскада классификаторов для обнаружения глаз
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

# Загрузика изображение и преобразуем его в оттенки серого
img = cv2.imread('faces/2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Обнаружение лиц на изображении
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Для каждого обнаруженного лица найдем глаза и измерьям их размер
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for index, (ex, ey, ew, eh) in enumerate(eyes):
        # Измерение расстояния между уголками глаз
        eye_corners = np.array(
            [(ex, ey), (ex+ew, ey), (ex, ey+eh), (ex+ew, ey+eh)])
        eye_distance = np.linalg.norm(eye_corners[0] - eye_corners[1])
        # Измерьям угол между уголками глаз и центром лица
        face_center = np.array([(x+w)/2, (y+h)/2])
        eye_center = np.array([(ex+ew)/2, (ey+eh)/2])
        eye_vector = eye_center - face_center
        face_vector = np.array([1, 0])
        angle = np.arccos(np.dot(eye_vector, face_vector) /
                          (np.linalg.norm(eye_vector) * np.linalg.norm(face_vector)))
        # Нарисуем круги в уголках глаз и покажите измерения
        # cv2.circle(roi_color, (ex+(ew//2), ey+(eh//2)), 3, (0, 255, 0), -1)
        cv2.putText(roi_color, "{:.2f}".format(
            eye_distance), (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1) # Distance:pixels
        
        cv2.putText(roi_color, "{:.2f}".format(
            angle), (ex, ey+eh+10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1) #Angle:  radians

        print(f"eye={index}, distance={eye_distance} pixels, angle={angle} radians")

# Вывод изображения с измерениями
cv2.imwrite('faces/out/3.jpg', img)

