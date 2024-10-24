import numpy as n
import cv2

from cvzone.HandTrackingModule import HandDetector
from keras.api.models import load_model

model = load_model("keras_model.h5")
labels = open("labels.txt", "r").readlines()

video = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

todo = 89
folder = "trained_images/THANKS"
counter = 0

previous = ""
msg = ""
nohandtime = 0
handshown = False

while True:

    success, img = video.read()
    hand, img = detector.findHands(img)

    if hand:

        if not handshown:
            handshown = True

        cv2.imshow("Image", img)
        image = cv2.resize(img, (224,224), interpolation=cv2.INTER_AREA)

        image = n.asarray(image,dtype=n.float32).reshape(1,224,224,3)

        image = (image/127.5)-1

        prediction = model.predict(image)
        index = n.argmax(prediction)
        class_name = labels[index]
        score = prediction[0][index]

        print(class_name, score)

        if score*100>90 and previous!=class_name:
            previous = class_name
            msg+=class_name

    else:
        if handshown:
            nohandtime+=1
            if nohandtime>100:
                handshown = False
                msg = ""
                nohandtime = 0




    

    
