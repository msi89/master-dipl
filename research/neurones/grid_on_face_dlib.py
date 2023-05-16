import cv2
import dlib

# Charger le détecteur de visage de dlib (pré-entrainé)
face_detector = dlib.get_frontal_face_detector()

# Charger l'image
image = cv2.imread('faces/lena.jpg')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détecter les visages dans l'image
faces = face_detector(gray)

# Boucler sur tous les visages détectés
for face in faces:
    # Obtenir les coordonnées du rectangle de délimitation du visage
    x, y, w, h = face.left(), face.top(), face.width(), face.height()

    # Définir le nombre de lignes et de colonnes de la grille
    num_rows = 10
    num_cols = 10

    # Calculer les dimensions d'une cellule de la grille
    cell_width = w // num_cols
    cell_height = h // num_rows

    # Tracer les lignes horizontales de la grille
    for i in range(1, num_rows):
        y_line = y + i * cell_height
        cv2.line(image, (x, y_line), (x + w, y_line), (5,5,5), 5)

    # Tracer les lignes verticales de la grille
    for j in range(1, num_cols):
        x_line = x + j * cell_width
        cv2.line(image, (x_line, y), (x_line, y + h), (5,5,5), 5)

# Save image
cv2.imwrite("result5.jpg", image)


