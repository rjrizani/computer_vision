import cv2
import numpy as np

image_path = 'rabit.jpeg'

image = cv2.imread(image_path)
color_range = {
    'red': ((0, 0, 200), (20, 20, 255)),
    'blue': ((100, 100, 0), (255, 255, 100)),
    'green': ((0, 200, 0), (100, 255, 100)),
    'yellow': ((0, 200, 200), (100, 255, 255)),
    'purple': ((200, 0, 200), (255, 100, 255)),
    'orange': ((0, 200, 100), (100, 255, 200)),
    'white': ((0, 0, 0), (255, 255, 255)),
    'black': ((0, 0, 0), (255, 255, 255)),
    'gray': ((0, 0, 0), (255, 255, 255))
}
color = input("Enter the color you want to detect: ")

def color_detection(image,lower_color, upper_color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result


if color in color_range.keys():
    result = color_detection(image, np.array(color_range[color][0]), np.array(color_range[color][1]))

    cv2.imshow('original image', image)

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Color not found")