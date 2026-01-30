# Emotion-Driven Meme Generator

This is a simple computer vision project that detects facial emotions using a webcam and displays a meme based on the detected expression.

The goal of this project was to understand how real-time face detection and emotion recognition work together in a practical application.

---

## What This Project Does

- Detects faces using YOLOv8  
- Recognizes emotions from the webcam feed  
- Displays a meme that matches the detected emotion  
- Runs in real time on a local machine  

---

## Technologies Used

- Python  
- OpenCV  
- YOLOv8  
- Deepface (Facial Emotion Recognition)  

---

## Project Structure

```
Emotion-Driven-Meme/
│
├── main.py        # Runs the application
├── detector.py    # Handles face and emotion detection
├── memes.py       # Selects memes based on emotion
├── memes/         # Meme images
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/hiianish/Emotion-Driven-Meme.git
cd Emotion-Driven-Meme
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Download the YOLOv8 face model

(Note: The model file is not included in the repository due to its size.)

### 4. Run the application

```
python main.py
```

The webcam will open and memes will change based on facial expressions.

---

## Purpose of This Project

This project was built as a learning exercise to explore:

- Real-time computer vision  
- Emotion detection  
- Working with pretrained models  
- Structuring a small AI project  

---

## Future Improvements

- Improve emotion accuracy  
- Add support for multiple faces  
- Create a web version  
- Enhance meme selection  

---

This project is created for learning and educational purposes.
