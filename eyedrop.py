import cv2
import numpy as np

image_ = cv2.imread('rabit.jpeg')
cv2.namedWindow('image')

def get_color_name(hue_value):
    for color_name, (lower, upper) in color_ranges.items():
        if lower[0] <= hue_value <= upper[0]:
            return color_name
    return None
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = image_[y,x]
        print("warna pixel yang diklik", image_[y,x])
        color_window = np.zeros((100,120,3), np.uint8)
        color_window[:] = [b,g,r]
        cv2.imshow('warna terdeteksi', color_window)

        hsv_frame = cv2.cvtColor(image_, cv2.COLOR_BGR2HSV)
        color_hue = hsv_frame[y,x,0]
        color_name = get_color_name(color_hue)
        if color_name:
            print("warna yang terdeteksi", color_name)


cv2.setMouseCallback('image', mouse_callback)

color_ranges = {
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


while True:
    cv2.imshow('image', image_)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()

