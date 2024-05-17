# Hand Gesture Recognition using Mediapipe and Random Forest

This project implements a hand gesture recognition system using Mediapipe for hand landmark detection and a Random Forest classifier for gesture classification. The project includes scripts for data collection, dataset creation, model training, and real-time gesture recognition.

## Table of Contents

- [Hand Gesture Recognition using Mediapipe and Random Forest](#hand-gesture-recognition-using-mediapipe-and-random-forest)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Collect Images](#collect-images)
    - [Create Dataset](#create-dataset)
    - [Train Classifier](#train-classifier)
    - [Test Classifier](#test-classifier)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Project Overview

This project provides a framework for recognizing hand gestures using a webcam. It leverages Mediapipe for detecting hand landmarks and uses a Random Forest classifier to recognize gestures based on the landmark positions.

## Features

- Collect images for training the model.
- Create a dataset with hand landmarks.
- Train a Random Forest classifier to recognize gestures.
- Real-time gesture recognition using a webcam.

## Installation

1. Clone the repository:

    ```sh
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2. Install the required packages:

    ```sh
    pip install opencv-python mediapipe scikit-learn numpy
    ```

## Usage

### Collect Images

1. Run the `collect_images.py` script to collect images for training:

    ```sh
    python collect_images.py
    ```

2. Follow the on-screen instructions to collect images for each class.

### Create Dataset

1. Run the `create_dataset.py` script to process the images and create a dataset:

    ```sh
    python create_dataset.py
    ```

2. This script will create a `data.pickle` file containing the hand landmarks and their corresponding labels.

### Train Classifier

1. Run the `train_classifier.py` script to train the Random Forest classifier:

    ```sh
    python train_classifier.py
    ```

2. This script will train the model and save it to a `model.p` file.

### Test Classifier

1. Run the `test_classifier.py` script to test the classifier in real-time using your webcam:

    ```sh
    python test_classifier.py
    ```

2. The script will display the webcam feed and recognize hand gestures in real-time.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and is well-documented.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please contact:

- **Your Name**
- **Your Email**
- **Your GitHub Profile**

Thank you for checking out the Hand Gesture Recognition project!
