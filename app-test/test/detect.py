import cv2


def detect(img_path='1.jpeg'):
    # Charger l'image du visage
    img = cv2.imread(img_path)

    # Charger le fichier de modèle de détection de visage
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

    # Parcourir les visages détectés
    for (x, y, w, h) in faces:
        # Extraire la région du visage
        face_img = img[y:y+h, x:x+w]

        # Convertir en niveaux de gris pour la symétrie
        gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

        # Calculer la symétrie
        symmetry = cv2.matchTemplate(
            gray[:, :w//2], cv2.flip(gray[:, w//2:], 1), cv2.TM_CCORR_NORMED)[0][0]

        # Afficher la symétrie
        print(f"La symétrie du visage {img_path} est de :", symmetry)


detect()
detect("2.webp")
