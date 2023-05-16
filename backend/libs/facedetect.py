import cv2
import dlib
import numpy as np
from schemas.asymetry import AsymmetryReport, FaceMeasure

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
            symmetry_status = "non-critical"
            symmetry_desc = "You must consult a doctor or a specialist"
        elif symmetry < 0.7:
            line_color = (255, 0, 0)
            symmetry_status = "normal"
            symmetry_desc = "Your face is normal"

        result.append(AsymmetryReport(
            symmetry=symmetry, descrition=symmetry_desc,
            status=symmetry_status))
        # cv2.rectangle(img, (x, y), (x+w, y+h), line_color, 2)
        # draw_eyes_landmarks(img, index, line_color)
        # draw_grid_on_image(img)

    # cv2.imwrite(output, img)
    # cv2.waitKey(0)
    # Retourner l'image avec les visages détectés
    return (result, len(faces))


# Fonction pour calculer la symétrie d'un visage
def calculateSymmetry(img):
    flip_img = cv2.flip(img, 1)
    diff_img = cv2.absdiff(img, flip_img)
    diff_mean = np.mean(diff_img)
    img_mean = np.mean(img)
    return diff_mean / img_mean


def getAsymetryMeasure(image_path) -> list[FaceMeasure]:
    # Chargement de l'image à évaluer
    # image_path = "faces/1.jpg"
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Détection des visages dans l'image
    rects = detector(gray, 0)

    result: list[FaceMeasure] = []

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

        result.append(FaceMeasure(
            face_width=face_width,
            face_height=face_height,
            left_eye_width=left_eye_width,
            right_eye_width=right_eye_width,
            nose_width=nose_width,
            mouth_width=mouth_width,
            proportionality=proportionality,
            horizontal_asymmetry=horizontal_asymmetry,
            vertical_asymmetry=vertical_asymmetry
        ))
        # # Affichage des résultats
        # print("Visage n°{}".format(i+1))
        # print(
        #     "- Asymétrie horizontale : {:.2f}%".format(horizontal_asymmetry * 100))
        # print(
        #     "- Asymétrie verticale : {:.2f}%".format(vertical_asymmetry * 100))
        # print("- Proportionnalité : {:.2f}%".format(proportionality * 100))
        # print("- face_width : {:.2f}".format(face_width))
        # print("- face_height : {:.2f}".format(face_height))
        # print("- left_eye_width : {:.2f}".format(left_eye_width))
        # print("- right_eye_width : {:.2f}".format(right_eye_width))
        # print("- nose_width : {:.2f}".format(nose_width))
        # print("- mouth_width : {:.2f}".format(mouth_width))

    return result


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


def grid_on_face_asymmetry(img_path, outpath=str):
    img = cv2.imread(img_path)
    # Detect faces in image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    # Loop over each face and calculate asymmetry
    for (x, y, w, h) in faces:
        # Compute face edges using Canny edge detection
        gray_face = gray[y:y+h, x:x+w]
        edges = cv2.Canny(gray_face, threshold1=30, threshold2=100)

        # Compute asymmetry based on edge differences between left and right
        # sides of face
        left_half = edges[:, :w//2]
        right_half = edges[:, w//2:]
        # Resize one half to have the same shape as the other half
        right_half = cv2.resize(
            right_half, (left_half.shape[1], left_half.shape[0]))
        asymmetry = np.sum(np.abs(left_half - right_half)) / \
            float(left_half.shape[0] * left_half.shape[1])

        print("asymetry: ", asymmetry)
        # Draw grid on face region if asymmetry is below threshold
        # if asymmetry < 0.2:
        if asymmetry < 30:
            # Define grid parameters
            rows = 10
            cols = 10
            grid_color = (5, 5, 5)  # Green color
            thickness = 5

            # Compute rectangle size based on grid size and face dimensions
            rect_height = h // rows
            rect_width = w // cols

            # Draw rectangles to form grid on face region
            for i in range(rows):
                for j in range(cols):
                    x_rect = x + j * rect_width
                    y_rect = y + i * rect_height
                    cv2.rectangle(
                        img,
                        (x_rect, y_rect),
                        (x_rect + rect_width, y_rect + rect_height),
                        grid_color,
                        thickness
                    )

    # Display image
    # filename, ext = os.path.splitext(img_path)
    # cv2.imwrite(f'{filename}.out{ext}', img)
    cv2.imwrite(outpath, img)


def draw_grid_on_image(imgpath, save=False):
    img = cv2.imread(imgpath)

    # Define grid parameters
    rows = 10
    cols = 10
    # grid_color = (0, 255, 0)  # Green color
    grid_color = (5, 5, 5)  # Gray color
    thickness = 5

    # Compute rectangle size based on grid size and image dimensions
    height, width, _ = img.shape
    rect_height = height // rows
    rect_width = width // cols

    # Draw rectangles to form grid
    for i in range(rows):
        for j in range(cols):
            x = j * rect_width
            y = i * rect_height
            cv2.rectangle(img, (x, y), (x + rect_width, y +
                                        rect_height), grid_color, thickness)
    if save:
        # Save image
        cv2.imwrite(imgpath, img)


def draw_grid_on_face(imgpath, save=False):
    # Load image and initialize face detector
    img = cv2.imread(imgpath)
    # face_cascade = cv2.CascadeClassifier(
    #     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    # Loop over each face and draw grid on face region
    for (x, y, w, h) in faces:
        # Define grid parameters
        rows = 10
        cols = 10
        # grid_color = (0, 255, 0)  # Green color
        grid_color = (5, 5, 5)  # Grey color
        thickness = 5

        # Compute rectangle size based on grid size and face dimensions
        rect_height = h // rows
        rect_width = w // cols

        # Draw rectangles to form grid on face region
        for i in range(rows):
            for j in range(cols):
                x_rect = x + j * rect_width
                y_rect = y + i * rect_height
                cv2.rectangle(img, (x_rect, y_rect), (x_rect + rect_width,
                                                      y_rect + rect_height), grid_color, thickness)

    if save:
        # Save image
        cv2.imwrite(imgpath, img)
