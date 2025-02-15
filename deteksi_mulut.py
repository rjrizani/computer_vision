import cv2

# Load the Haar Cascade Classifier for mouth detection
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

if mouth_cascade.empty():
    print("Error: Unable to load mouth cascade classifier")
else:
    # Load the image
    image = cv2.imread('pinguin.jpeg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect mouths in the image
    mouths = mouth_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected mouths
    for (x, y, w, h) in mouths:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('Mouth Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()