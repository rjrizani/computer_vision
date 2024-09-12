import cv2
image_path = 'pinguin.jpeg'

image = cv2.imread(image_path)

clone = image.copy()

(x1,y1, x2, y2) = cv2.selectROI("select rectangular area", image, fromCenter=False, showCrosshair=True)

selected_area = clone[y1:y1+y2, x1:x1+x2]  #ranga area yang dipilih

cv2.imshow("selected area", selected_area)
cv2.waitKey(0)
cv2.destroyAllWindows()
