import cv2
import numpy as np
import os
import csv
import math

codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))

def process(ip_image):
    angle=0.00
    hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV)
    LowerRange_RedDot = np.array([0, 255, 255])
    UpperRange_RedDot = np.array([0, 255, 255])
    Mask_RedDot = cv2.inRange(hsv, LowerRange_RedDot, UpperRange_RedDot)
    #cv2.imshow("window", ip_image)
    #red_dot = cv2.bitwise_not(Mask_RedDot)
    #cv2.imshow("Red Dot Masked", red_dot)

    #green circle detection
    LowerRange_RedDot = np.array([30, 255, 255])
    UpperRange_RedDot = np.array([255, 255, 255])
    Mask_GreenDot = cv2.inRange(hsv, LowerRange_RedDot, UpperRange_RedDot)
    #cv2.imshow("window", ip_image)
    #green_dot = cv2.bitwise_not(Mask_GreenDot)
    #cv2.imshow("Green Dot Masked", green_dot)
    
    res=cv2.add(Mask_GreenDot,Mask_RedDot)
    resInverted = cv2.bitwise_not(res)
    cv2.imshow('result',resInverted)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    detected_circles = cv2.HoughCircles(resInverted,cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,param2 = 10, minRadius = 1, maxRadius = 40)
    print("1st detection")
    print(detected_circles)
    print("**********************************")
    l,b=np.shape(resInverted)
    print("length   " +str(l) +"   breath   " +str(b))
    a=detected_circles-[l/2,b/2,0]
    print(a)
    print("**********************************")
    z=a[0][0][0]*a[0][1][0]+a[0][0][1]*a[0][1][1]
    print(z)
    y=math.sqrt(a[0][0][0]**2+a[0][0][1]**2)
    print(y)
    x=math.sqrt(a[0][1][0]**2+a[0][1][1]**2)
    print(x)
    #cos_theta=z/(x*y)
    #print(cos_theta/math.pi)
    angle=math.acos(z/(x*y))
    print(angle)
    angle=(angle*180)/math.pi
    if(angle<0):
        angle+=180
    print(angle)
    #if detected_circles is not None:
     #   detected_circles = np.uint16(np.around(detected_circles))
      #  print(detected_circles)
    return angle

def main():
    i=1
    line = []
    for image_name in os.listdir(images_folder_path):
        print(image_name)
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        print(ip_image.shape)
        A = process(ip_image)
        line.append([str(i), image_name , str(A)])
        i+=1
    print(line)
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()
if __name__ == '__main__':
    main()
