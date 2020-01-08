import os
import numpy as np
import cv2
from numpy.fft import fft2, ifft2
from scipy.signal import gaussian, convolve2d
import matplotlib.pyplot as plt
import cv2.aruco as aruco
from aruco_lib import *
images_folder_path = os.path.abspath(os.path.join('..', 'Videos'))
def blur(img, kernel_size = 3):
        dummy = np.copy(img)
        h = np.eye(kernel_size) / kernel_size
        dummy = convolve2d(dummy, h, mode = 'valid')
        return dummy


def wiener_filter(img, kernel, K):
        kernel /= np.sum(kernel)
        dummy = np.copy(img)
        dummy = fft2(dummy)
        kernel = fft2(kernel, s = img.shape)
        kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
        dummy = dummy * kernel
        dummy = np.real(ifft2(dummy))
        return dummy

def gaussian_kernel(kernel_size = 20):
        h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
        h = np.dot(h, h.transpose())
        h /= np.sum(h)
        return h
def wiener_deconvolution(signal, kernel):
        "lambd is the SNR"
        kernel= np.eye(20) / 20
        kernel = np.hstack((kernel, np.zeros(len(signal) - len(kernel)))) # zero pad the kernel to same length
        H = fft(kernel)
        deconvolved = np.real(ifft(fft(signal)*np.conj(H)/(H*np.conj(H))))
        return deconvolved
    
def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


if __name__ == '__main__':
        # Load image and convert it to gray scale
        file_name = os.path.join(images_folder_path, "original.png") 
        img11 = rgb2gray(plt.imread(file_name) )
        val=31
        cap = cv2.VideoCapture(images_folder_path+"/"+"ArUco_bot.mp4")
        ## getting the frames per second value of input video
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_seq = int(val)*fps
        ## setting the video counter to frame sequence
        cap.set(1,frame_seq)
        ## reading in the frame
        ret, frame = cap.read()
        img=frame[:720,:1280]
        # Blur the image
##      alpha=0.75
##      beta=0
##      img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

        brightness=89
        contrast=73
        shadow = brightness
        highlight = 255
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
        img = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
        img = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)




        
##      cv2.imshow("Extracted image",img)
##      blurred_img0 = blur(img[:,:,0], kernel_size = 20)
##      blurred_img1 = blur(img[:,:,1], kernel_size = 20)
##      blurred_img2 = blur(img[:,:,2], kernel_size = 20)
        temp=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##      cv2.imshow("Extracted gray image",temp)
        # Apply Wiener Filter
        
        #kernel = np.eye(20) / 20
        kernel = np.zeros((20,20))
        kernel[:,10]=54
        print(kernel)
        k=1000
        id_list=None
        
        K=0.1
        b,g,r = cv2.split(img)
        filtered_img0 = wiener_filter(b, kernel,K)
        filtered_img1 = wiener_filter(g, kernel,K)
        filtered_img2 = wiener_filter(r, kernel,K)
##      filtered_img= cv2.cvtColor(tempf,cv2.COLOR_GRAY2BGR)
        # Display results
##      cv2.imshow("filtered image",tempf)
##      cv2.imwrite('./tempf.png',tempf)
        merge=cv2.merge((filtered_img0,filtered_img1,filtered_img2)).astype('uint8')
        k=500
        while id_list==None:
                filtered_img0 = wiener_filter(b, kernel,K=0.0001*k)
                filtered_img1 = wiener_filter(g, kernel,K=0.0001*k)
                filtered_img2 = wiener_filter(r, kernel,K=0.0001*k)
                merge=cv2.merge((filtered_img0,filtered_img1,filtered_img2)).astype('uint8')
                id_list = detect_Aruco(merge)
                print(id_list,k)
                k=k-1
        print(id_list,k)
        cv2.imshow("filtered image dd",merge)
        
        display = [img, temp,  tempf, merge]
        label = ['Original Image', 'Motion Blurred Image',  'Wiener Filter applied',"merge"]
        
        print (id_list)
        fig = plt.figure(figsize=(14, 112))

        for i in range(len(display)):
                fig.add_subplot(2, 2, i+1)
                plt.imshow(display[i], cmap = 'gray')
                plt.title(label[i])
        plt.show()
