import cv2
import numpy as np
import math
import pyautogui
import mediapipe as mp

def map_to_screen(x, y, width, height):
    screen_width, screen_height = pyautogui.size()
    mapped_x = np.interp(x, [0, width], [0, screen_width])
    mapped_y = np.interp(y, [0, height], [0, screen_height])
    return mapped_x, mapped_y

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

PINCH_DISTANCE_THRESHOLD = 50

cam = cv2.VideoCapture(0)

cam.set(3, 1280)
cam.set(4, 720)

cv2.namedWindow('Hand Tracking')
hands = mp_hands.Hands(max_num_hands=1)

while True:
    success, frame = cam.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
            index_finger_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
            thumb_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * frame.shape[1])
            thumb_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * frame.shape[0])

            mapped_x, mapped_y = map_to_screen(index_finger_x, index_finger_y, frame.shape[1], frame.shape[0])

            dist = math.sqrt((index_finger_x-thumb_x)**2 + (index_finger_y - thumb_y)**2)

            if dist < PINCH_DISTANCE_THRESHOLD:
                pyautogui.click()
                print("Pinch Detected: 00x1")
                

            pyautogui.moveTo(mapped_x, mapped_y)    

    
        

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
cam.release()
cv2.destroyAllWindows()