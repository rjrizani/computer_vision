import cv2
import tkinter as tk
from tkinter import filedialog
import  numpy as np

root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(title='Choose an image', filetypes=(("image", "*.jpg"), ("all files", "*.*")))


selected_points = []
dots =None
def mouse_callback(event, x, y, flags, param):
    global selected_points
    if event == cv2.EVENT_LBUTTONUP:
        if len(selected_points) < 4:
            selected_points.append((x, y))
            cv2.circle(dots, (x, y), 5, (0,0,255), -1)
            print(selected_points)
            if len(selected_points) == 4:
                warped_image = four_point_transform(original_image.copy(), np.array(selected_points))
                cv2.imshow('warped image', warped_image)

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)

    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    print(rect)
    return rect


if image_path != "":
    global display_image
    original_image = cv2.imread(image_path)
    height, width = original_image.shape[:2]
    scale = 600/max(height, width)
    display_image = cv2.resize(original_image, None, fx=scale, fy=scale)
    dots = np.zeros_like(display_image)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',mouse_callback)

    while True:
        combined_image = cv2.addWeighted(display_image, 0.7, dots, 0.3, 0)
        cv2.imshow('image combined', combined_image)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break




cv2.waitKey(0)
cv2.destroyAllWindows()