import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from pickle file
with open('./data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

# Convert data and labels to numpy arrays
data = np.array(data_dict['data'], dtype=object)
labels = np.array(data_dict['labels'], dtype=str).astype(int)

# Pad data to ensure consistent length
max_len = max(len(sample) for sample in data)
padded_data = np.array([np.pad(sample, (0, max_len - len(sample)), 'constant') for sample in data])

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(padded_data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train SVM
svm_model = SVC()
svm_model.fit(x_train, y_train)

# Predict on the test set
y_pred = svm_model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'{accuracy * 100:.2f}% of samples were classified correctly!')

# Save the trained model to a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump({'model': svm_model}, f)
