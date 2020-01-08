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
    ## placeholder image
    sector_image = np.ones(ip_image.shape[:2],np.uint8)*255
    ## check value is white or not
    print(sector_image[0,0])

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
    #====================================
    
    hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV)
    LowerRange = np.array([0, 4, 0])
    UpperRange = np.array([0, 127, 255])

    Mask = cv2.inRange(hsv, LowerRange, UpperRange)

    Height, Width = Mask.shape[:2]
    
    # Up-Down check
    FoundCircle = 0
    for i in range(int(Height/2)-5):
        if Mask[(int(Height/2)-i), int(Width/2)] != 0:
            if FoundCircle == 0:
                InnerCircleRadiusUp = i
            FoundCircle = 1

        if FoundCircle == 1:
            if Mask[(int(Height/2)-i), int(Width/2)] == 0:            
                FoundCircle = 2
                OuterCircleRadiusUp = i
                break

    FoundCircle = 0
    for i in range(int(Height/2)-5):
        if Mask[(int(Height/2)+i), int(Width/2)] != 0:
            if FoundCircle == 0:
                InnerCircleRadiusDown = i
            FoundCircle = 1

        if FoundCircle == 1:
            if Mask[(int(Height/2)+i), int(Width/2)] == 0:            
                FoundCircle = 2
                OuterCircleRadiusDown = i
                break

    # Left-Right check
    FoundCircle = 0
    for j in range(int(Width/2)-5):
        if Mask[int(Height/2), (int(Width/2)-j)] != 0:
            if FoundCircle == 0:
                InnerCircleRadiusLeft = i
            FoundCircle = 1

        if FoundCircle == 1:
            if Mask[int(Height/2), (int(Width/2)-j)] == 0:            
                FoundCircle = 2
                OuterCircleRadiusLeft = i
                break

    FoundCircle = 0
    for j in range(int(Width/2)-5):
        if Mask[int(Height/2), (int(Width/2)+j)] != 0:
            if FoundCircle == 0:
                InnerCircleRadiusRight = i
            FoundCircle = 1

        if FoundCircle == 1:
            if Mask[int(Height/2), (int(Width/2)+j)] == 0:            
                FoundCircle = 2
                OuterCircleRadiusRight = i
                break


    List1 = [OuterCircleRadiusUp, OuterCircleRadiusDown, OuterCircleRadiusLeft, OuterCircleRadiusRight] 
    List1.sort()
    FinalRadiusOut = List1[1]

    List2 = [InnerCircleRadiusUp, InnerCircleRadiusDown, InnerCircleRadiusLeft, InnerCircleRadiusRight] 
    List2.sort()
    FinalRadiusIn = List2[1]

    

        
    ColourOfCircle = (0,255,0)
    ip_image = cv2.circle(ip_image, (int(Height/2), int(Width/2)), FinalRadiusOut, ColourOfCircle, -1)
    ip_image = cv2.circle(ip_image, (int(Height/2), int(Width/2)), FinalRadiusIn, (0,0,255), -1)

    
    #cv2.imshow("Masked", Mask)
    #cv2.imshow("Input", ip_image)
    
    for i in range(Height):
        for j in range(Width):
            if (ip_image[i,j][0] == ColourOfCircle[0]) and (ip_image[i,j][1] == ColourOfCircle[1]) and (ip_image[i,j][2] == ColourOfCircle[2]):
                sector_image[i,j] = Mask[i,j]


    sector_image[:,:] = 255 - sector_image[:,:]
    kernel = np.ones((3,3),np.uint8)
    sector_image = cv2.erode(sector_image,kernel,iterations = 1)
    sector_image = cv2.dilate(sector_image,kernel,iterations = 1)
    sector_image[:,:] = 255 - sector_image[:,:]
    
   ## Your Code goes here
    ###########################
    cv2.imshow("window", sector_image)
    cv2.waitKey(0);
    cv2.destroyAllWindows() # Remove it at the end
    return sector_image




    
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
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        sector_image = process(ip_image)
        ## saving the output in  an image of said name in the Generated folder
        cv2.imwrite(generated_folder_path+"/"+"image_"+str(i)+"_fill_in.png", sector_image)
        i+=1


    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
