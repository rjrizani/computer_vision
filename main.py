import cv2
import tkinter as tk

from tkinter import filedialog

def show_image():
    image_path = 'sample.jpeg'
    image = cv2.imread(image_path)


    gray_image = apply_gray_scale_filter(image)
    cv2.imshow('image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_gray_scale_filter(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def show_image2():
    root = tk.Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(title='Choose an image', filetypes=(("image", "*.jpg"), ("all files", "*.*")))

    if image_path== "":
        print("no image selected")
        return

    #read the file
    image = cv2.imread(image_path)

    #show the image
    cv2.imshow('Image', image)

    #apply gray scale filter
    gray_image = apply_gray_scale_filter(image)
    cv2.imshow('Gray Image', gray_image)

    #wait until key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image2()