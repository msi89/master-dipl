
import dlib
import cv2


face_detector = dlib.get_frontal_face_detector()

landmark_predictor = dlib.shape_predictor('../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat')

image = cv2.imread('faces/lena.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_detector(gray)

for face in faces:
    # Prédiction des points du visage
    landmarks = landmark_predictor(gray, face) 
    # Parcourir les points du visage et les dessiner sur l'image
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 15, (5, 5, 5), -1)
    # for n in range(1, 68): # dessiner le visage
    #     x1 = landmarks.part(n - 1).x
    #     y1 = landmarks.part(n - 1).y
    #     x2 = landmarks.part(n).x
    #     y2 = landmarks.part(n).y
    #     cv2.line(image, (x1, y1), (x2, y2), (5, 5, 5), 10)
   

cv2.imwrite('result2.jpg', image)

