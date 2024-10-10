import cv2
import numpy as np
import matplotlib.pyplot as plt

image_part = 'pinguin.jpeg'
original_image = cv2.imread(image_part)

height, width = original_image.shape[:2]
scale = 600 / max(height, width)
display_image = cv2.resize(original_image, None, fx=scale, fy=scale)

cv2.imshow('image resized', display_image)

red_histogram = cv2.calcHist([display_image], [0], None, [256], [0, 256])
green_histogram = cv2.calcHist([display_image], [1], None, [256], [0, 256])
blue_histogram = cv2.calcHist([display_image], [2], None, [256], [0, 256])

plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(red_histogram, color='r')
plt.title('Red Histogram')

plt.subplot(3, 1, 2)
plt.plot(green_histogram, color='g')
plt.title('green Histogram')

plt.subplot(3, 1, 3)
plt.plot(blue_histogram, color='b')
plt.title('blue Histogram')

plt.tight_layout()
plt.show()
