import cv2
import dlib

# Charger le détecteur de visage de dlib (pré-entrainé)
face_detector = dlib.get_frontal_face_detector()

# Charger le prédicteur de points clés de dlib (pré-entrainé)
landmark_predictor = dlib.shape_predictor('../backend/assets/landmarks/shape_predictor_68_face_landmarks.dat')


def get_detected_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return face_detector(gray)

