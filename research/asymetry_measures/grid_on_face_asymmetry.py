import cv2
import numpy as np
import os


def grid_on_face_asymmetry(img_path, outpath=str):
    img = cv2.imread(img_path)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    # Loop over each face and calculate asymmetry
    for (x, y, w, h) in faces:
        # Compute face edges using Canny edge detection
        gray_face = gray[y:y+h, x:x+w]
        edges = cv2.Canny(gray_face, threshold1=30, threshold2=100)

        # Compute asymmetry based on edge differences between left and right sides of face
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
                    cv2.rectangle(img, (x_rect, y_rect), (x_rect + rect_width,
                                                          y_rect + rect_height), grid_color, thickness)

    # Display image
    # filename, ext = os.path.splitext(img_path)
    # cv2.imwrite(f'{filename}.out{ext}', img)
    cv2.imwrite(outpath, img)


photos = [
    "faces/analyst/1/Lena_1.jpg",
    "faces/analyst/1/Lena_2.jpg",
    "faces/analyst/1/Lena_3_v2.jpg",
]
# Load image and initialize face detector


# for p in photos:
#     grid_on_face_asymmetry(p)

grid_on_face_asymmetry(
    photos[2], "faces/results/grid_on_face_asymmetry.out.jpg")
