import os
import pickle
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# Initialize MediaPipe Hands solution
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Directory containing data
DATA_DIR = './data2'

# Lists to store data and labels
data = []
labels = []

# Iterate over each directory in DATA_DIR
for directory in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, directory)
    
    # Iterate over each image in the directory
    for img_name in os.listdir(dir_path):
        img_path = os.path.join(dir_path, img_name)
        
        # Load image and convert to RGB
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Process the image to detect hand landmarks
        results = hands.process(img_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(
                    img_rgb, 
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                
                # Collect landmark coordinates
                x_coords = [landmark.x for landmark in hand_landmarks.landmark]
                y_coords = [landmark.y for landmark in hand_landmarks.landmark]
                
                # Normalize landmark coordinates
                min_x = min(x_coords)
                min_y = min(y_coords)
                normalized_landmarks = [(x - min_x, y - min_y) for x, y in zip(x_coords, y_coords)]
                
                # Flatten normalized coordinates and store in data
                data.append([coord for point in normalized_landmarks for coord in point])
                labels.append(directory)

# Save data and labels to a pickle file
with open('data2.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
