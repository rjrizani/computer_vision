import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = cv2.imread('android.png', cv2.IMREAD_COLOR)  # Read image
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale


recognized_text = pytesseract.image_to_string(grey_image)  # Recognize text
print("recognized text")
print(recognized_text)

_, binary_image = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
countours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_with_contours = image.copy()
cv2.drawContours(image_with_contours, countours, -1, (0, 255, 0), 3)


cv2.imshow('Binary image', binary_image)
cv2.imshow('Image with contours', image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()