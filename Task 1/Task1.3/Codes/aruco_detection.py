import numpy as np
import cv2
import cv2.aruco as aruco
from aruco_lib import *

frame = cv2.imread("aruco25.jpg")#cv2.VideoCapture(0)

robot_state=0
det_aruco_list = {}

if(True):
	#ret,frame = cap.read()
	# print frame.shape
	det_aruco_list = detect_Aruco(frame)
	print(det_aruco_list)
	if det_aruco_list:
		img = mark_Aruco(frame,det_aruco_list)
		robot_state = calculate_Robot_State(img,det_aruco_list)
		print(robot_state)        
		# print min(robot_state.keys()), robot_state[(min(robot_state.keys()))]
		# cv2.circle(img,(255,50),1,(0,255,0),2)
		# cv2.imshow('marker', img)
	cv2.imshow('image',frame)
	cv2.imwrite("output.jpg",frame)


cv2.destroyAllWindows()
