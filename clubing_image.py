import cv2
import numpy as np

image1 = cv2.imread('rabit.jpeg')
image2 = cv2.imread('pinguin.jpeg')

# print hight and width of image


def combine_image(image1, image2):
    print("image1 rabit shape", image1.shape)
    print("height image1 rabit ", image1.shape[0])
    print("width image1 rabit ", image1.shape[1])
    print("image2  pinguin shape", image2.shape)

    if  image1.shape != image2.shape:
        resize_image = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
        image2 = resize_image

    combine_image = (image1 + image2)
    #combine_image = np.maximum(image1, image2)          #maximum pixel
   # combine_image = np.minimum(image1, image2)

    alpa = 0.2
    combine_image = cv2.addWeighted(image1, alpa, image2, 1 - alpa, 0)

    concanated_image = np.vstack((image1, image2))


    cv2.imshow('image1', image1)
    cv2.imshow('image2', image2)
    cv2.imshow('combine_image', combine_image)
    cv2.imshow('concanated_image', concanated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


combine_image(image1, image2)