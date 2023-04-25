import cv2
import numpy as np


def get_gradient():
    """gradient calculation"""
    # Read image
    img = cv2.imread('2.webp')
    img = np.float32(img) / 255.0

    # Calculate gradient
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
    # Python Calculate gradient magnitude and direction ( in degrees )
    mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
    return mag, angle


mag, angle = get_gradient()
print("=====mag====\n", mag)
print("====angle====\n", angle)
