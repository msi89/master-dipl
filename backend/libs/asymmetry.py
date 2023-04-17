import cv2
import dlib
import numpy as np
from schemas.asymetry import AsymmetryReport

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    'assets/landmarks/shape_predictor_68_face_landmarks.dat')
# Charger le classificateur de visage pré-entraîné
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def asymetry_detection(img, output: str) -> tuple:
    # Convertir l'image en niveaux de gris pour la détection de visage
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    result: list[AsymmetryReport] = []
    # Parcourir chaque visage détecté et calculer sa symétrie
    for index, (x, y, w, h) in enumerate(faces):
        face_roi = gray[y:y+h, x:x+w]
        symmetry = calculateSymmetry(face_roi)

        line_color = (0, 255, 0)
        symmetry_status = "good"
        symmetry_desc = "Your face symmetry is perfect"
        if symmetry < 0.1:
            line_color = (0, 0, 255)
            symmetry_status = "critical"
            symmetry_desc = "We recommand you take contact of a specialist"
        elif symmetry < 0.5:
            line_color = (0, 150, 255)
            symmetry_status = "warning"
            symmetry_desc = "You must consult a doctor or a specialist"
        elif symmetry < 0.7:
            line_color = (255, 0, 0)
            symmetry_status = "normal"
            symmetry_desc = "Your face is normal"

        result.append(AsymmetryReport(
            symmetry=symmetry, descrition=symmetry_desc,
            status=symmetry_status))
        # cv2.rectangle(img, (x, y), (x+w, y+h), line_color, 2)
        draw_eyes_landmarks(img, index, line_color)

    cv2.imwrite(output, img)
    cv2.waitKey(0)
    # Retourner l'image avec les visages détectés
    return (result, len(faces))


def draw_eyes_landmarks(img, index, color: tuple = (0, 255, 0)):
    # Initialiser le détecteur de visage et les points de repère du visage

    # Détecter les visages dans l'image
    faces = detector(img, 1)
    face = faces[index]
    landmarks = predictor(img, face)
    # Dessiner un cercle sur chaque point de repère du visage
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(img, (x, y), 2, color, -1)


# Fonction pour calculer la symétrie d'un visage
def calculateSymmetry(img):
    flip_img = cv2.flip(img, 1)
    diff_img = cv2.absdiff(img, flip_img)
    diff_mean = np.mean(diff_img)
    img_mean = np.mean(img)
    return diff_mean / img_mean
