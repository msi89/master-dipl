from lib.dlibcv import cv2,  landmark_predictor, get_detected_faces

import numpy as np

image = cv2.imread('faces/lena.jpg')
faces = get_detected_faces(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Vérifier si un visage a été détecté
if len(faces) > 0:
    # Sélectionner le premier visage détecté
    face = faces[0]
    
    # Détection des points clés du visage
    landmarks = landmark_predictor(gray, face)
    
    # Extraire les coordonnées des points clés
    points = []
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        points.append((x, y))
    
    # Calcul des différences entre les points clés des côtés gauche et droit du visage
    differences = []
    for i in range(0, 68 // 2):
        x_diff = points[i][0] - points[68 - i - 1][0]
        y_diff = points[i][1] - points[68 - i - 1][1]
        differences.append((x_diff, y_diff))
    
    # Afficher les différences entre les points clés
    for diff in differences:
        print("Différence en x : ", diff[0])
        print("Différence en y : ", diff[1])
    
    asymmetry = np.mean(np.abs(differences))
    
    print("Asymétrie du visage :", asymmetry)

else:
    print("Aucun visage détecté dans l'image.")

