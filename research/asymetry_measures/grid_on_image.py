import cv2
# Load image
img = cv2.imread('faces/analyst/1/Lena_3_v2.jpg')

# Define grid parameters
rows = 10
cols = 10
grid_color = (0, 255, 0)  # Green color
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

# Save image
cv2.imwrite("faces/results/grid_on_image_out.jpg", img)
