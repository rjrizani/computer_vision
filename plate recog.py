import cv2
import os
import numpy as np
import imutils
import pytesseract
import pandas as pd
import time
import re

image_folder = 'plat/images/'
actual_data = pd.read_csv('plat/actual_data.csv', sep=';')
print(actual_data.columns)
#print(actual_data)

data_to_append = []


def process_image(image_path):
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=500)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    countours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours = sorted(countours, key=cv2.contourArea, reverse=True)[:30]

    for c in countours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            NumberPlateCnt = approx
            break
    mask = np.zeros(gray_image.shape, np.uint8)
    mask = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)

    new_image = cv2.bitwise_and(image, image, mask=mask)
    config = ('-l eng --oem 1 --psm 3')
    detected_plate = pytesseract.image_to_string(new_image, config=config)

    detected_plate = detected_plate.replace(' ', '').replace('\n', '')
    detected_plate = re.sub('[^a-zA-Z0-9]', '', detected_plate).upper()

    return detected_plate

for image_file in os.listdir(image_folder):
    if image_file.endswith(('jpg', 'jpeg', 'png')):
        image_path = os.path.join(image_folder, image_file)
        print(image_path)


        actual_plate = actual_data[actual_data['image_file'] == image_file]['actual_number_plate'].values[0]

        print(actual_plate)

        detected_plate = process_image(image_path)
        print("detected plate number",detected_plate)

        if actual_plate == detected_plate:
            print('correct')
        else:
            print('incorrect')
        time.sleep(1)
        print()


        def calculate_accuracy(detected_plate, actual_plates):
            detected_chars = list(detected_plate.lower())
            actual_chars = list(actual_plates.lower())
            correct_chars = [d == a for d, a in zip(detected_chars, actual_chars)]
            return (sum(correct_chars) / len(correct_chars)) * 100


        accuracy = calculate_accuracy(detected_plate, actual_plate)
        print("Accuracy: {:.2f}%".format(accuracy))

        table = []

        table.append(
            {'date': time.asctime(time.localtime(time.time())),
            'actual_number_plate': actual_plate,
            'detected_number_plate': detected_plate,
            'accuracy': accuracy,}
        )

        existing_data = pd.DataFrame(columns=['date', 'actual_number_plate', 'detected_number_plate', 'accuracy'])
        new_data = pd.DataFrame(table)

        existing_data = existing_data.dropna(axis=1, how='all')
        new_data = new_data.dropna(axis=1, how='all')

        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv('plat/actual_data.csv', index=False)

        print(updated_data)













