import cv2
import numpy as np
from detector import detect_emotion
from memes import get_memes

cap =  cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        break

    emotion,boxes = detect_emotion(frame)
    meme = get_memes(emotion)


    for(x1,y1,x2,y2) in boxes:
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        if emotion:
            cv2.putText(frame,emotion,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

    
    memes_resized = cv2.resize(meme,(400,frame.shape[0]))
    compined = np.hstack((frame,memes_resized))

    cv2.imshow("just chill",compined)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows  
