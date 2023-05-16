import cv2
# Load image
img = cv2.imread('faces/lena.jpg')

# Define grid parameters
rows = 10
cols = 10
grid_color = (5, 5, 5)  # Green color
thickness = 2

# Compute rectangle size based on grid size and image dimensions
height, width, _ = img.shape
rect_height = height // rows
rect_width = width // cols

# Draw rectangles to form grid
for i in range(rows):
    for j in range(cols):
        x = j * rect_width
        y = i * rect_height
        cv2.rectangle(img, (x, y), (x + rect_width, y + rect_height), grid_color, thickness)

# Save image
cv2.imwrite("face_out.jpg", img)