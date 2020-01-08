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
import random

import cv2.aruco as aruco
from aruco_lib import *
import copy



########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Videos'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################

def wiener_filter(img, kernel, K):
	kernel /= np.sum(kernel)
	dummy = np.copy(img)
	dummy = np.fft.fft2(dummy)
	kernel = np.fft.fft2(kernel, s = img.shape)
	kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
	dummy = dummy * kernel
	dummy = np.real(np.fft.ifft2(dummy))
	return dummy

    
def process(ip_image):
    ###########################
    ## Your Code goes here
    ###########################
    id_list = []
    
    ip_image=ip_image[:720,:1280]

        ## Brightness and contrast control
    brightness=89
    contrast=73
    highlight = 255
    alpha_b = (highlight - brightness)/255
    gamma_b = brightness
    ip_image = cv2.addWeighted(ip_image, alpha_b, ip_image, 0, gamma_b)
    f = 131*(contrast + 127)/(127*(131-contrast))
    alpha_c = f
    gamma_c = 127*(1-f)
    ip_image = cv2.addWeighted(ip_image, alpha_c, ip_image, 0, gamma_c)

        # Kernel
    kernel = np.zeros((20,20))
    kernel[:,10]=54
    b,g,r = cv2.split(ip_image)
    K=0.0440
##    temp=cv2.cvtColor(ip_image,cv2.COLOR_BGR2GRAY)
##    temp_filter=wiener_filter(temp,kernel,K).astype('uint8')
##    cv2.imshow('tem',temp_filter)
    
    filtered_img0 = wiener_filter(b, kernel,K)
    filtered_img1 = wiener_filter(g, kernel,K)
    filtered_img2= wiener_filter(r, kernel,K)
    image=cv2.merge((filtered_img0,filtered_img1,filtered_img2))
    
    image=image.astype('uint8') 

    cv2.waitKey(0) # waits until a key is pressed
##    cv2.imshow('Bilateral Blurring', bilateral) 
##    cv2.waitKey(0) 
##    cv2.destroyAllWindows() 
##    cv2.imshow("window", outp-filterut)
##    cv2.waitKey(0);
    temp_filter=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    det_aruco_list = detect_Aruco(image)
	#print(det_aruco_list)
    if det_aruco_list:
            ip_image = mark_Aruco(image,det_aruco_list)
            id_list = calculate_Robot_State(ip_image,det_aruco_list)
            print(id_list)
		# print min(robot_state.keys()), robot_state[(min(robot_state.keys()))]
		# cv2.circle(img,(255,50),1,(0,255,0),2)
		# cv2.imshow('marker', img)
    cv2.imshow('image',ip_image)
    print(id_list)
    cv2.imwrite(generated_folder_path+"/"+"aruco_with_id.png",image)
    return ip_image, id_list[25]


    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main(val):
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## reading in video 
    cap = cv2.VideoCapture(images_folder_path+"/"+"ArUco_bot.mp4")
    ## getting the frames per second value of input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    ## getting the frame sequence
    frame_seq = int(val)*fps
    ## setting the video counter to frame sequence
    cap.set(1,frame_seq)
    ## reading in the frame
    ret, frame = cap.read()
    ## verifying frame has content
    print(frame.shape)    ## display to see if the frame is correct
    cv2.imshow("window", frame)
    cv2.waitKey(0);
    ## calling the algorithm function
    op_image, aruco_info = process(frame)
    ## saving the output in  a list variable
    line = [str(i), "Aruco_bot.jpg" , str(aruco_info[0]), str(aruco_info[3])]
    ## incrementing counter variable
    i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'output.csv', 'w') as writeFile:
        print("About to write csv")
        writer = csv.writer(writeFile)
        writer.writerow(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    #main(input("time value in seconds:"))
    main(31)
