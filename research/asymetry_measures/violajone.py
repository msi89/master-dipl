import cv2

# загрузить изображение
image = cv2.imread('faces/2.jpg')

# преобразовать изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# загрузка каскадного классификатора Хаара для распознавания лиц
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# обнаружить лица на изображении
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# просмотреть все обнаруженные лица
for (x, y, w, h) in faces:
   # нарисовать прямоугольник вокруг обнаруженного лица
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # загрузка каскадного классификатора Хаара для распознавания глаз
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml')
    # обнаружить глаза на лице
    eyes = eye_cascade.detectMultiScale(
        gray[y:y+h, x:x+w], scaleFactor=1.1, minNeighbors=5)
    # петля через обнаруженные глаза
    for (ex, ey, ew, eh) in eyes:
        # нарисуйте прямоугольник вокруг каждого обнаруженного глаза
        cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)

# отобразить изображение с обнаруженными маркерами лица

cv2.imwrite('faces/out/7.jpg', image)
cv2.waitKey(0)
