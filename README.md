# American Sign Language (ASL) Recognition Project

This project recognizes American Sign Language (ASL) alphabet using computer vision and machine learning techniques. It utilizes OpenCV to capture images and Mediapipe for hand landmark detection. The model is trained using Support Vector Classifier (SVC) to predict ASL letters from hand gestures.

## Project Structure

- **`create_dataset.py`**: Script to create a dataset for training the model using captured hand images.
- **`create_dataset2.py`**: Same as `create_dataset.py`, but for handling specific cases where ASL letters are visually similar.
- **`data_collector.py`**: Collects data and saves hand images for specific ASL letters.
- **`data_collector2.py`**: Same as `data_collector.py`, for handling visually similar letters.
- **`predict.py`**: Predicts the ASL letter based on hand gestures using the trained model.
- **`train_model.py`**: Trains the SVC model for general ASL alphabet recognition.
- **`train_model2.py`**: Trains a second SVC model for better accuracy on visually similar letters.
- **`requirements.txt`**: Lists the dependencies required for the project.

## Why Two Models?

In American Sign Language (ASL), certain letters are visually similar, such as:

- **A**, **E**
- **M**, **N**
- **S**, **T**

To handle these similarities and improve prediction accuracy, we use two models:

1. **Main Model**: The first model is a general ASL recognition model trained on the entire alphabet. It can predict the ASL letter based on hand gestures. However, due to the visual similarities between some letters, the main model might incorrectly predict one of the 6 similar letters, such as **A**, **E**, **M**, **N**, **S**, or **T**.

2. **Second Model**: When the main model's prediction falls into one of these 6 similar letters, we pass that result through a second, specialized model that has been trained specifically on these visually similar letters. This model is able to distinguish between them more accurately and provide the correct prediction.

By using this two-step approach, we ensure higher accuracy in recognizing ASL letters, particularly those that look alike but have different meanings. The main model gives an initial prediction, and the second model fine-tunes it for those cases where visual similarity is a concern.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Farees04/signDetection.git
    cd signDetection
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

- To collect data for training:
  ```bash
  python data_collector.py
  ```
- To collect data for visually similar letters:
  ```bash
  python data_collector2.py
  ```
- To train the model for general ASL recognition:
  ```bash
  python train_model.py
  ```
- To train the second model for visually similar letters:
  ```bash
  python train_model2.py
  ```
- To predict the ASL letter:
  ```bash
  python predict.py
  ```
 
  
