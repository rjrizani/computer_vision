import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

cap = cv2.VideoCapture(0)

def detect_face(image, faces):
    for (x, y, w, h) in faces:
       cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
       roi_color= image[y:y+h, x:x+w]
       roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
       smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
       cv2.putText(image, "smile", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return(image)



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = smile_cascade.detectMultiScale(gray, 1.1, 4)


    detect = detect_face(frame, faces)
    cv2.imshow('frame', detect)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
