import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)#since we are only using one hand


offset = 20
imgSize = 300

folder = "Data/U"
counter = 0

while True:
    success, img = cap.read()
    hands ,img = detector.findHands(img)#for complete hand joints for better recognition
    if hands :
        hand = hands[0]#because we are only using onehand hence hands[0]is used
        x,y,w,h = hand['bbox']#bounding box for croping the image
        
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255#it means its value is 0to255& multiplied by 25 to get white img otherwise it is black in color
        
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]#croping image[height,width]
        
        imgCropShape = imgCrop.shape
        
        
        
        aspectRatio = h/w
        
        if aspectRatio>1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))#wCal=width,imgSize=height in White
            imgResizeShape = imgResize.shape
            wGap = math.ceil((300-wCal)/2)
            imgWhite[:,wGap:wCal+wGap] = imgResize#putting imageCrop matric on ImgWhite matrices
        
        
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize,hCal))#wCal=width,imgSize=height in White
            imgResizeShape = imgResize.shape
            hGap = math.ceil((300-hCal)/2)
            imgWhite[hGap:hCal+hGap,:] = imgResize  
        
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    
    if key == ord("s"):
        counter +=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)#time.time() gives unique value
        print(counter)
