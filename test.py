import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
#import tensorflow
#import keras
#from tensorflow.keras.models import load_model
import cv2 
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np 
import math 

np.set_printoptions(suppress=True)

#model = load_model("keras_Model.h5", compile=False)

# Load the labels
#class_names = open("labels.txt", "r").readlines()

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 2)
classifier = Classifier("keras_model.h5", "labels.txt")
offset = 20
imgSize = 300
counter = 0

labels = ["Hello", "How are you", "I love you", "Thank you","What your name", "Yes"]

while True :
    Success, img = cap.read()
    imgOutput = img.copy()
    hands , img = detector.findHands(img)

    if hands :
        hand = hands[0]
        x,y,w,h = hand['bbox']
        
        imgWhite = np.ones((imgSize,imgSize,3), np.uint8)*255

        imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
        imgCropShape = imgCrop.shape

        aspectRatio = h / w
        try:

            if aspectRatio > 1:
               k = imgSize / h
               wCal = math.ceil(k * w)
               imgResize = cv2.resize(imgCrop, (wCal, imgSize))
               imgResizeShape = imgResize.shape
               wGap = math.ceil((imgSize-wCal)/2)
               imgWhite[:, wGap: wCal + wGap] = imgResize
               prediction, index = classifier.getPrediction(imgWhite, draw=False)
               print(prediction, index)

            else :
             
               k = imgSize / w
               hCal = math.ceil(k * h)
               imageResize = cv2.resize(imgCrop, (imgSize, hCal))
               imgResizeShape = imageResize.shape
               hGap = math.ceil((imgSize - hCal) / 2)
               imgWhite[hGap: hCal + hGap, :] = imageResize
               prediction, index = classifier.getPrediction(imgWhite, draw=False)
               print(prediction, index)

            cv2.rectangle(imgOutput, (x-offset, y-offset-70), (x -offset+400, y - offset+60-50),(0,255,0),cv2.FILLED)

            cv2.putText(imgOutput,labels[index],(x,y-30),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2) 
            cv2.rectangle(imgOutput,(x-offset,y-offset),(x + w + offset, y+h + offset),(0,255,0),4)   
        
            cv2.imshow('ImageCrop', imgCrop)
            cv2.imshow('ImageWite', imgWhite)
        except Exception as e:
            print(f"Error processing hands: {e}")
    
    cv2.imshow('Image', imgOutput)
    if cv2.waitKey(1)& 0xFF == ord('d') :
        
       break

#cap.release()
#cv2.destroyAllWindows()