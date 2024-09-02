import cv2

image_path = 'sample.jpeg'

image = cv2.imread(image_path)
'''

def crop_image(image, x, y, w, h):
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

cropped_image = crop_image(image, 0, 0, 200, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

def resize_image(image, scale_percentage):
    width = int(image.shape[1] * scale_percentage / 100)
    height = int(image.shape[0] * scale_percentage / 100)
    resized_image = cv2.resize(image, (width, height))
    return resized_image

resized_image = resize_image(image, 50)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
def rotate_image(image, angle):
    center = (image.shape[1] / 2, image.shape[0] / 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return rotated_image


rotated_image = rotate_image(image, 45)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()