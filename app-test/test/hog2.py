# import cv2
# import dlib
# import numpy as np

# # Chargement du détecteur de visage et de landmarks
# face_detector = dlib.get_frontal_face_detector()
# landmark_predictor = dlib.shape_predictor(
#     '../../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat')

# # Chargement de l'image
# img = cv2.imread('faces/2.jpg')

# # Conversion en niveau de gris
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Détection de visage en utilisant le détecteur de visage Dlib
# faces = face_detector(gray)

# # Itération à travers chaque visage détecté
# for face in faces:
#     # Détection de landmarks
#     landmarks = landmark_predictor(gray, face)

#     # Conversion des landmarks en un tableau numpy
#     landmarks = np.array(
#         [(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)])

#     # Affichage des landmarks sur l'image
#     for (x, y) in landmarks:
#         cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

# # Affichage de l'image avec les landmarks détectés
# cv2.imwrite('faces/out/2.jpg', img)
# cv2.waitKey(0)


import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    "../../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat")

image = cv2.imread("faces/2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for face in faces:
    landmarks = predictor(gray, face)
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

cv2.imwrite("faces/out/2333.jpg", image)
