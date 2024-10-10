import cv2
from ultralytics import YOLO

image_path = 'cat_dog.jpeg'
image= cv2.imread(image_path)

model = YOLO("yolov8m.pt")
result = model.predict(source=image_path, show=True, conf=0.5, save=False)
result = result[0]

print(result.names)
print(len(result.boxes))

for box in result.boxes:
    class_id = result.names[box.cls[0].item()]
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    conf = round(box.conf[0].item(), 2)

    #detail
    print("object type : ", class_id)
    print("coordinates : ", cords)
    print("confidence : ", conf)
    print("\n")

    if conf > 0.2:
        x1, y1, x2, y2 = cords
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        label =f"{class_id} {conf}"
        image =cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
