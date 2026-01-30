from ultralytics import YOLO
from deepface import DeepFace
import cv2

model = YOLO("yolov8n-face-lindevs.pt")

emotion_last = None
stable_count = 0
stable_threshold = 3
frame_count = 0

def detect_emotion(frame):
    global emotion_last,stable_count,frame_count

    result = model(frame,verbose = False)

    emotion_output = emotion_last
    boxes_output =[]


    for r in result:
        boxes= r.boxes.xyxy.cpu().numpy()

        for box in boxes:
            x1, y1, x2, y2 = map(int,box)
            face = frame[y1:y2, x1:x2]
            face = cv2.resize(face, (224, 224))


            if face.size == 0:
                continue

            if frame_count % 30 == 0:
                try:
                    result = DeepFace.analyze(face,actions=['emotion'],enforce_detection=False,detector_backend='opencv')
                    emotion = result[0]['dominant_emotion']

                    if emotion == emotion_last:
                        stable_count += 1
                    else:
                        stable_count = 0

                    emotion_last = emotion

                    if stable_count >= stable_threshold:
                        emotion_output = emotion

                except:
                    pass
            
            boxes_output.append([x1,y1,x2,y2])
    

    frame_count += 1
    return emotion_output,boxes_output