import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

video_part = "mobile.mp4"
cap = cv2.VideoCapture(video_part)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow('frame', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()