import cv2
import numpy as np
import os
import glob

def partA():
    ImgDir = "../Images/"
    DataPath = os.path.join(ImgDir,'*g')
    Files = glob.glob(DataPath)
    for FilePath in Files:
        # file names are stored in FilePath one by one (Relative path
        # is stored)
        print(FilePath)
        InputImage = cv2.imread(FilePath)

        Height, Width, Channel = InputImage.shape
        # Height, Width and number of Channels in image is stored in
        # variables "Height", "Width" and "Channel"
        print(Height)
        print(Width)
        print(Channel)

        B_Value = InputImage[int(Height/2), int(Width/2)][0]
        G_Value = InputImage[int(Height/2), int(Width/2)][1]
        R_Value = InputImage[int(Height/2), int(Width/2)][2]
        # B, G, R values are stored in respective variables.     
        print(B_Value)
        print(G_Value)
        print(R_Value)

        print()
    pass

def partB():
    Cat_Image = cv2.imread("../Images/cat.jpg")

    Height, Width, Channel = Cat_Image.shape

    for i in range(Height):
        for j in range(Width):
            Cat_Image[i, j][0] = 0
            Cat_Image[i, j][1] = 0

    cv2.imwrite("../Generated/cat_red.jpg", Cat_Image)

    pass

def partC():
    Flowers_Image = cv2.imread("../Images/flowers.jpg")
    
    FourC_Image = cv2.cvtColor(Flowers_Image, cv2.COLOR_BGR2BGRA)

    Height, Width, Channel = FourC_Image.shape
        
    for i in range(Height):
        for j in range(Width):
            FourC_Image[i, j][3] *= 0.5

    cv2.imwrite("../Generated/flowers_alpha.png", FourC_Image)
    
    pass

def partD():
    Horse_Image = cv2.imread("../Images/horse.jpg")

    Gray = Horse_Image
    Gray = cv2.cvtColor(Gray, cv2.COLOR_BGR2GRAY)
   
    Height, Width, Channel = Horse_Image.shape

    for i in range(Height):
        for j in range(Width):
            B = Horse_Image[i, j][0]
            G = Horse_Image[i, j][1]
            R = Horse_Image[i, j][2]

            Gray[i, j] = int(((0.3*R) + (0.59*G) + (0.11*B)))

    cv2.imwrite("../Generated/horse_gray.jpg", Gray)
    
    pass

partA()
partB()
partC()
partD()
