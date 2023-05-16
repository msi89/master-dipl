import dlib
import cv2
import numpy as np

# Charger le détecteur de visage de dlib (HOG-based)
detector = dlib.get_frontal_face_detector()

# Charger le prédicteur de points clés de visage de dlib
predictor = dlib.shape_predictor(
    "../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat")

# Charger l'image
image_path = "faces/lena.jpg"
image = cv2.imread(image_path)

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détecter les visages dans l'image
faces = detector(gray)

# Boucle sur les visages détectés
for face in faces:
    # Prédire les points clés du visage
    landmarks = predictor(gray, face)
    # Coordonnées des points clés
    keypoint_coordinates = []
    for i in range(0, landmarks.num_parts):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        keypoint_coordinates.append((x, y))
        # Dessiner les points clés sur l'image
        # cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

# Convertir les coordonnées des points clés en un tableau numpy
train_keypoints = np.array(keypoint_coordinates)

# Afficher les coordonnées des points clés
print("Coordonnées des points clés d'entraînement :")
print(train_keypoints[0])
