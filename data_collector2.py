import os
import cv2

# Directory to store the data
DATA_DIR = './data2'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Parameters
number_of_classes = 5
dataset_size = 150

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Loop through each class
for class_idx in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(class_idx))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Starting data collection for class {class_idx}')

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press "Q" to start collecting data', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    # Collect dataset_size images for the current class
    for img_idx in range(dataset_size):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        img_path = os.path.join(class_dir, f'{img_idx}.jpg')
        cv2.imwrite(img_path, frame)

cap.release()
cv2.destroyAllWindows()