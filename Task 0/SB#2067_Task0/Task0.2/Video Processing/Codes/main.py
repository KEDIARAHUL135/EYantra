import cv2
import numpy as np
import os

def partA():
    Count = 0;
    cap = cv2.VideoCapture("../Videos/RoseBloom.mp4")

    while True:
        ret, InputFrame = cap.read()
        
        if not ret:
            print('\nCannot Read Video\n')
            exit(1)
        Count += 1
        
        if Count == 125:
            ret, InputFrame = cap.read()

            if not ret:
                print('\nCannot Read Video\n')
                exit(2)
            
            cv2.imwrite("../Generated/frame_as_6.jpg", InputFrame)
            cap.release()
            break
    
    pass

def partB():

    Frame = cv2.imread("../Generated/frame_as_6.jpg")

    Frame[:, :,0] = 0
    Frame[:, :,1] = 0

    cv2.imwrite("../Generated/frame_as_6_red.jpg", Frame)
    pass

partA()
partB()
