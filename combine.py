import cv2
import numpy as np

image1 = cv2.imread('wajah.jpeg')
image2 = cv2.imread('sample.jpeg')
image3 = cv2.imread('rabit.jpeg')
image4 = cv2.imread('pinguin.jpeg')

'''
print("height of image1", image1.shape[0])
print("width of image1", image1.shape[1])

print("height of image2", image2.shape[0])
print("width of image2", image2.shape[1])

image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
blended = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

cv2.imshow('Combined images', blended)
'''

size = (200,200)

image1 = cv2.resize(image1, size)
image2 = cv2.resize(image2, size)
image3 = cv2.resize(image3, size)
image4 = cv2.resize(image4, size)

top_row = cv2.hconcat([image1, image2])
bottom_row = cv2.hconcat([image3, image4])
blended = cv2.vconcat([top_row, bottom_row])

cv2.imshow('Combined images', blended)

cv2.waitKey(0)
cv2.destroyAllWindows()

