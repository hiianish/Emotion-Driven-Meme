import cv2

memes_map = {
    "happy": "memes/happy.jpg",
    "sad": "memes/sad.jpg",
    "angry": "memes/angry.jpg",
    "surprise": "memes/surprise.jpg",
    "neutral": "memes/neutral.jpg",
    "fear": "memes/sad.jpg",
    "disgust": "memes/angry.jpg"
}


current_meme = cv2.imread("memes/neutral.jpg")


def get_memes(emotion):
    global current_meme

    if emotion is None:
        return current_meme
    

    memes_path = memes_map.get(emotion)

    if memes_path:
        img =cv2.imread(memes_path)
        if img is not None:
            current_meme = img
    return current_meme