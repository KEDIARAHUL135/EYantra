###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv




########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))

######################################################################
## Self made Functions   -- made by Kedia
######################################################################
def CallbackFunction(var):
    return


def FindCentrePoint(Image):
    #=======================================
    # Code for finding centre of dots
    HorCentreHeightStart = 0
    HorCentreHeightEnd = 0
    HorCentre = 0
    FoundFirstPixel = 0
    
    Height, Width = Image.shape[:2]
    
    for i in range(Height):
        for j in range(Width):
            if Image[i, j] != 0:
                if FoundFirstPixel == 0:
                    StartPixelHor = j
                    FoundFirstPixel = 1
                if FoundFirstPixel == 1:
                    EndPixelHor = j

            elif FoundFirstPixel == 1:
                break

        if FoundFirstPixel == 1:
            HorCentreHeightStart = i
            HorCentre = int((EndPixelHor+StartPixelHor)/2)
            for i in range(Height-HorCentreHeightStart):
                if Image[HorCentreHeightStart + i, HorCentre] != 0:
                    HorCentreHeightEnd = HorCentreHeightStart + i
                else:
                    break
            break

    # cv2.line(Image, (HorCentre, HorCentreHeightStart), (HorCentre, HorCentreHeightEnd), (0,0,0), 1)
    # cv2.imshow("Masked", Image)

    # Height of circle is (HorCentreHeightEnd-HorCentreHeightStart+1)
    # Position is [((HorCentreHeightEnd+HorCentreHeightStart)/2),(HorCentre)]
    '''print()
    print()
    print(HorCentreHeightEnd-HorCentreHeightStart+1)
    print(HorCentreHeightStart)
    print(HorCentreHeightEnd)
    print()
    print()'''
    
    # End of Code for finding centre of dots
    #=======================================
    return int((HorCentreHeightEnd+HorCentreHeightStart)/2), HorCentre

######################################################################
## End of Self made Functions   -- made by Kedia
######################################################################



############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    angle = 0.00
    #=================================
    # Code for finding red and green dots.. uncomment to apply
    '''cv2.namedWindow("Trackbar")
    cv2.createTrackbar("LR_1", "Trackbar", 0, 255, CallbackFunction)
    cv2.createTrackbar("LR_2", "Trackbar", 0, 255, CallbackFunction)
    cv2.createTrackbar("LR_3", "Trackbar", 0, 255, CallbackFunction)
    cv2.createTrackbar("UR_1", "Trackbar", 0, 255, CallbackFunction)
    cv2.createTrackbar("UR_2", "Trackbar", 0, 255, CallbackFunction)
    cv2.createTrackbar("UR_3", "Trackbar", 0, 255, CallbackFunction)
    hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV)

    while(cv2.waitKey(1) != 27):
        LR_1 = cv2.getTrackbarPos("LR_1", "Trackbar")
        LR_2 = cv2.getTrackbarPos("LR_2", "Trackbar")
        LR_3 = cv2.getTrackbarPos("LR_3", "Trackbar")
        UR_1 = cv2.getTrackbarPos("UR_1", "Trackbar")
        UR_2 = cv2.getTrackbarPos("UR_2", "Trackbar")
        UR_3 = cv2.getTrackbarPos("UR_3", "Trackbar")
        LowerRange = np.array([LR_1, LR_2, LR_3])
        UpperRange = np.array([UR_1, UR_2, UR_3])

        Mask = cv2.inRange(hsv, LowerRange, UpperRange)

        cv2.imshow("Masked", Mask)'''
    # End of code for finding dots
    # OBS - For all 3 images
    #   Red Dot Bounds - [0, 255, 255] -> [0, 255, 255]
    #   Green Dot Bounds - [16-60, 255, 255] -> [255, 255, 255]
    #====================================

    #====================================
    # Code for Printing two dots 
    hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV)

    LowerRange_RedDot = np.array([0, 255, 255])
    UpperRange_RedDot = np.array([0, 255, 255])
    Mask_RedDot = cv2.inRange(hsv, LowerRange_RedDot, UpperRange_RedDot)

    LowerRange_GreenDot = np.array([30, 255, 255])
    UpperRange_GreenDot = np.array([255, 255, 255])
    Mask_GreenDot = cv2.inRange(hsv, LowerRange_GreenDot, UpperRange_GreenDot)

    # TotalMask = Mask_RedDot[:,:] + Mask_GreenDot[:,:]
    # cv2.imshow("FinalMask", TotalMask)
    
    # End of code for Printing two dots
    #=====================================

    #=====================================
    # Code for finding centre point
    '''Height, Width = ip_image.shape[:2]
    cv2.line(ip_image, (int(Width/2), 0), (int(Width/2), (Height-1)), (0,0,0), 1)
    cv2.line(ip_image, (0, int(Height/2)), ((Width-1), int(Height/2)), (0,0,0), 1)
    cv2.imwrite("Check_Output.png", ip_image)'''
    # End of code for finding centre point
    # OBS - centre point at - (Width/2, Height/2)
    #======================================

    Height, Width = ip_image.shape[:2]
    RD_row, RD_col = FindCentrePoint(Mask_RedDot)
    GD_row, GD_col = FindCentrePoint(Mask_GreenDot)
    WD_row = int(Height/2)
    WD_col = int(Width/2)

    ip_image[RD_row, RD_col] = 0
    ip_image[GD_row, GD_col] = 0
    ip_image[WD_row, WD_col] = 0
    
    ## Your Code goes here
    ###########################
    cv2.imshow("window", ip_image)
    cv2.waitKey(0);

    # Remove destroyAllWindows Line at the end... it is written by Kedia
    cv2.destroyAllWindows()
    return angle, ip_image




    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A, FinalImage = process(ip_image)
        cv2.imwrite(image_name, FinalImage)
        ## saving the output in  a list variable
        line.append([str(i), image_name , str(A)])
        ## incrementing counter variable
        i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
