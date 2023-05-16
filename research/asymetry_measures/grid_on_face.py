import cv2

# Load image and initialize face detector
img = cv2.imread('faces/analyst/1/Lena_3_v2.jpg')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Loop over each face and draw grid on face region
for (x, y, w, h) in faces:
    # Define grid parameters
    rows = 10
    cols = 10
    grid_color = (0, 255, 0)  # Green color
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

# Save image
cv2.imwrite("faces/results/grid_on_face_out.jpg", img)
