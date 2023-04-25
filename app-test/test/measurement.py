import cv2
import dlib
import numpy as np

# Chargement du modèle de détection des points clés du visage
predictor_path = "../../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def measure(image_path):
    # Chargement de l'image à évaluer
    # image_path = "faces/1.jpg"
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Détection des visages dans l'image
    rects = detector(gray, 0)

    # Boucle sur chaque visage détecté dans l'image
    for (i, rect) in enumerate(rects):
        # Détection des points clés du visage
        shape = predictor(gray, rect)
        shape = np.array([(p.x, p.y) for p in shape.parts()])

        # Mesure de la distance entre les points clés pour évaluer l'asymétrie et la proportionnalité faciale
        left_eye = shape[36:42]
        right_eye = shape[42:48]
        nose = shape[27:36]
        mouth = shape[48:68]
        face_width = np.abs(left_eye[0][0] - right_eye[-1][0])
        face_height = np.abs(nose[0][1] - mouth[-1][1])
        left_eye_width = np.abs(left_eye[-1][0] - left_eye[0][0])
        right_eye_width = np.abs(right_eye[-1][0] - right_eye[0][0])
        nose_width = np.abs(nose[-1][0] - nose[0][0])
        mouth_width = np.abs(mouth[-1][0] - mouth[0][0])

        # Calcul de l'asymétrie et de la proportionnalité faciale
        horizontal_asymmetry = np.abs(
            left_eye_width - right_eye_width) / face_width
        vertical_asymmetry = np.abs(nose_width - mouth_width) / face_height
        proportionality = (left_eye_width + right_eye_width +
                           nose_width + mouth_width) / face_width

        # Affichage des résultats
        print("Visage n°{}".format(i+1))
        print(
            "- Asymétrie horizontale : {:.2f}%".format(horizontal_asymmetry * 100))
        print(
            "- Asymétrie verticale : {:.2f}%".format(vertical_asymmetry * 100))
        print("- Proportionnalité : {:.2f}%".format(proportionality * 100))
        print("- face_width : {:.2f}".format(face_width))
        print("- face_height : {:.2f}".format(face_height))
        print("- left_eye_width : {:.2f}".format(left_eye_width))
        print("- right_eye_width : {:.2f}".format(right_eye_width))
        print("- nose_width : {:.2f}".format(nose_width))
        print("- mouth_width : {:.2f}".format(mouth_width))


print("1.jpg*****************************")
measure("faces/1.jpg")
print("2.jpg*****************************")
measure("faces/2.jpg")
print("3.jpg*****************************")
measure("faces/3.jpg")
print("4.jpg*****************************")
measure("faces/4.jpg")
print("5.jpg*****************************")
measure("faces/5.jpg")
