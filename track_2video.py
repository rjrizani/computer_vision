import cv2
from ultralytics import YOLO
import threading
import queue

model1 = YOLO("yolov8n.pt")
model2 = YOLO("yolov8n-seg.pt")

video_file1 = "mobile.mp4"
video_file2 = "mobile2.mp4"

frame_queue1 = queue.Queue()
frame_queue2 = queue.Queue()
def run_tracker_in_thread(filename, model, frame_queue):
    video = cv2.VideoCapture(filename)
    frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for _ in range(frames):
        ret, frame = video.read()
        if ret:
            result = model.track(source=frame)
            res_plotted = result[0].plot()
            frame_queue.put(res_plotted)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    video.release()

tracker_thread1 = threading.Thread(target=run_tracker_in_thread, args=(video_file1, model1, frame_queue1))
tracker_thread2 = threading.Thread(target=run_tracker_in_thread, args=(video_file2, model2, frame_queue2))

tracker_thread1.start()
tracker_thread2.start()

while True:
    if not frame_queue1.empty():
        cv2.imshow('frame1', frame_queue1.get())
    if not frame_queue2.empty():
        cv2.imshow('frame2', frame_queue2.get())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

