import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)  # Adjust parameters as needed
mp_drawing = mp.solutions.drawing_utils

# Initialize Video Capture
cap = cv2.VideoCapture(0)  # 0 for default webcam, or provide video file path
TF_ENABLE_ONEDNN_OPTS=0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror-like effect (optional)
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (MediaPipe needs RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Access landmark coordinates (example: index finger tip)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])

            # You can now use the x, y coordinates for your project logic
            # Example: Draw a circle at the fingertip
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            # Example: Print coordinates (for debugging)
            # print(f"Index finger tip: x={x}, y={y}")


            # --- Gesture Recognition Logic (Example: Thumb Up/Down) ---
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]  # Thumb knuckle

            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]


            if thumb_tip.y < thumb_ip.y and index_tip.y < index_tip.x: # Thumb is up (crude check, improve this!)
                cv2.putText(frame, "Thumb Up!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif thumb_tip.y > thumb_ip.y and index_tip.y < index_tip.x: # Thumb is down (crude check, improve this!)
                cv2.putText(frame, "Thumb Down!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Add more gesture recognition logic here...


    # Display the frame
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()