import cv2
import numpy as np
import matplotlib.pyplot as plt

image_part = 'pinguin.jpeg'
original_image = cv2.imread(image_part)

height, width = original_image.shape[:2]
scale = 600 / max(height, width)
display_image = cv2.resize(original_image, None, fx=scale, fy=scale)

cv2.imshow('image resized', display_image)

histogram = cv2.calcHist([display_image], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.grid()
plt.show()

