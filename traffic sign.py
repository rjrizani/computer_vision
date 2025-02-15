import cv2
import numpy as np

# Define color ranges for traffic signs (adjust these based on your images)
red_lower = np.array([160, 100, 100])  # Example: Red lower bound in HSV
red_upper = np.array([180, 255, 255])  # Example: Red upper bound in HSV

blue_lower = np.array([100, 50, 50])  # Example: Blue lower bound in HSV
blue_upper = np.array([130, 255, 255])  # Example: Blue upper bound in HSV

# Load the image
image_path = "sign/blue.jpeg"  # Replace with your image path
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not open or read image file: {image_path}")
    exit()


# Convert to HSV color space (more robust for color detection)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create masks for red and blue (you can add more colors)
red_mask = cv2.inRange(hsv, red_lower, red_upper)
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)


# Combine masks if needed (e.g., if a sign has both red and blue)
# combined_mask = cv2.bitwise_or(red_mask, blue_mask)  # Example, uncomment if needed

# Apply morphological operations (optional, to reduce noise)
kernel = np.ones((5, 5), np.uint8)  # Adjust kernel size as needed
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
# combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)  # Uncomment if using combined mask


# Find contours in the masks
contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours_combined, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Uncomment if using combined mask


# Process detected contours (e.g., draw bounding boxes)
for contour in contours_red:
    area = cv2.contourArea(contour)
    if area > 500:  # Adjust area threshold as needed
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red box
        cv2.putText(img, "Red Sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Label

for contour in contours_blue:
    area = cv2.contourArea(contour)
    if area > 500:  # Adjust area threshold as needed
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue box
        cv2.putText(img, "Blue Sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Label

# ... (Add similar loops for other colors/combined masks)


# Display the result
cv2.imshow("Traffic Sign Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()