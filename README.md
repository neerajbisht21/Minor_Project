🚀 **Hand Gesture Recognition System**
======================================

Tagline: "Unlock the power of hand gestures with our AI-powered system"

**Description**
---------------

The Hand Gesture Recognition System is a Python-based project that utilizes OpenCV and machine learning algorithms to recognize and classify various hand gestures. The system is designed to be flexible and adaptable, allowing users to train the model with their own dataset and customize the recognition process to suit their specific needs.

Using a combination of computer vision and machine learning techniques, the system can detect and recognize various hand gestures, such as hand shapes, finger positions, and movements. The system is capable of recognizing gestures in real-time, making it a powerful tool for applications such as gaming, education, and assistive technology.

**Features**
------------

1. 📊 **Real-time Hand Detection**: The system uses a HandDetector module to detect and track hand movements in real-time.
2. 🤖 **Machine Learning-based Classification**: Classifies detected hand gestures into predefined categories.
3. 📁 **Customizable Model Training**: Train the model using your own dataset.
4. ✋ **Multi-Finger Support**: Supports multi-finger gestures.
5. 📈 **High Accuracy**: Reliable tool for gesture recognition.
6. 🕹️ **Real-time Feedback**: Adjust gestures with instant feedback.
7. ✋ **Hand Shape Recognition**: Detects various hand shapes.
8. 👉 **Finger Movement Recognition**: Recognizes pointing, swiping, tapping, etc.
9. 🔄 **Hand Rotation Recognition**: Supports hand rotation detection.
10. 🧠 **Multi-Modal Support**: Works with video, image, and audio.

**Tech Stack**
-------------

| Frontend | Backend | Tools |
|----------|---------|-------|
| Python   | OpenCV, Keras, TensorFlow | NumPy, Matplotlib |

**Project Structure**
--------------------

```
test2.py
datacollection.py
README.md
Model/keras_model.h5
Model/labels.txt
requirements.txt
```

- `test2.py`: Main script to run gesture recognition.
- `datacollection.py`: For collecting and preprocessing training data.
- `README.md`: Project documentation.
- `Model/`: Pre-trained model and labels.
- `requirements.txt`: Python dependencies.

**How to Run**
--------------

1. 📦 Install packages: `pip install -r requirements.txt`
2. 🏗️ Run: `python test2.py`
3. 📱 Customize or extend as needed

**Testing Instructions**
-------------------------

1. ✅ Unit Testing: Use `pytest`
2. 🔗 Integration Testing: Use `pytest`
3. 🔄 End-to-End Testing: Use `pytest`

**Screenshots**
---------------

📸 ![Screenshot](./Screenshot%202025-04-05%20123701.png)

**API Reference**
------------------

- `HandDetector(maxHands=1)`: Initialize hand detection.
- `Classifier(model_path, labels_path)`: Load model and labels.
- `hand_detector.detect_hand(frame)`: Detect hands in frame.
- `classifier.classify_hand(hand)`: Classify hand gesture.

**Author**
----------

- 👤 Neeraj Singh Bisht

**License**
-----------

This project is licensed under the MIT License.
