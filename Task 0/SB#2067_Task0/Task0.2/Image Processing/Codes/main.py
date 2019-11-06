import cv2
import numpy as np
import os


def partA():
    ImgDir = "../Images/"
    Data=np.array([[0,0,0,0,0,0,0]])
    Files = [f for f in os.listdir(ImgDir) if os.path.isfile(os.path.join(ImgDir, f))]
    for FileName in Files:
        # file names are stored in FilePath one by one (Relative path
        # is stored)
        FilePath= ImgDir+ FileName
        InputImage = cv2.imread(FilePath)
        Height, Width, Channel = InputImage.shape
        # Height, Width and number of Channels in image is stored in
        # variables "Height", "Width" and "Channel"
        B_Value = InputImage[int(Height/2), int(Width/2)][0]
        G_Value = InputImage[int(Height/2), int(Width/2)][1]
        R_Value = InputImage[int(Height/2), int(Width/2)][2]
        # B, G, R values are stored in respective variables.
        ImgData=[FileName,Height,Width,Channel,B_Value,G_Value,R_Value]
        Data= np.append(Data,[ImgData],axis=0)
    Data=np.delete(Data,0,axis=0)
    # print(Data)
    np.savetxt("../Generated/stats.csv", Data, delimiter=",",fmt='%s')
    pass

def partB():
    Cat_Image = cv2.imread("../Images/cat.jpg")

    Height, Width, Channel = Cat_Image.shape
    
    Cat_Image[:, :, 0] = 0
    Cat_Image[:, :, 1] = 0
    cv2.imwrite("../Generated/cat_red.jpg", Cat_Image)

    pass

def partC():
    Flowers_Image = cv2.imread("../Images/flowers.jpg")
    
    FourC_Image = cv2.cvtColor(Flowers_Image, cv2.COLOR_BGR2BGRA)
    
    FourC_Image[:, :, 3] = FourC_Image[:, :, 3] * 0.5
    
    cv2.imwrite("../Generated/flowers_alpha.png", FourC_Image)
    
    pass

def partD():
    Horse_Image = cv2.imread("../Images/horse.jpg")
    Height, Width, Channel = Horse_Image.shape
    
    Gray = np.zeros((Height, Width), np.uint8)

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
