import time

import cv2
from ultralytics import YOLO
import numpy as np


model = YOLO("yolov8x.pt")
video_width = 845
video_height = 480
cap = cv2.VideoCapture("orang.mp4")

while True:
    poeple_count = set()
    ret, frame = cap.read()
    print(type(frame))
    print(ret)
    if not ret:
        break

    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.track(rgb_img, persist=True, verbose=False)

    for i in range(len(results[0].boxes)):
        x1, y1, x2, y2 = results[0].boxes.xyxy[i]
        score = results[0].boxes.conf[i]
        cls = results[0].boxes.cls[i]               #cek confidence score, class and id
        ids = results[0].boxes.id[i]

        x1, y1, x2, y2, score, cls, ids = int(x1), int(y1), int(x2), int(y2), float(score), int(cls), int(ids)

        if score < 0.5  or cls !=0:
            continue

        poeple_count.add(ids)
        cx, cy = int(x1/2 + x2/2), int(y1/2 + y2/2)   #kordinat titik tengah
        cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1) #menampilkan garis melingkar
        print(poeple_count)
        people_count_text = "People count  " + str(len(poeple_count))
        cv2.putText(frame, people_count_text,(0,video_height-10), 0, 1,(0,128,0),1)

        cv2.imshow("frame", frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #time.sleep(000)


cap.release()
cv2.destroyAllWindows()
