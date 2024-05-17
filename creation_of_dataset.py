import os
import pickle
import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.2)

DATA_DIR = './data'
data = []
labels = []

# Function to process an image and extract hand landmarks
def process_image(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            data_aux = []
            for landmark in hand_landmarks.landmark:
                data_aux.extend([landmark.x, landmark.y])
            return data_aux
    return None

# Loop through each folder and select 100 images
for dir_ in os.listdir(DATA_DIR):
    img_count = 0
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        if img_count >= 200:
            break
        data_aux = process_image(os.path.join(DATA_DIR, dir_, img_path))
        if data_aux:
            data.append(data_aux)
            labels.append(dir_)
            img_count += 1

# Save the data and labels to a pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
