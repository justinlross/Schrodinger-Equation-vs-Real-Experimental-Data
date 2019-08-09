# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:29:50 2019

@author: Justin
"""

import cv2
import os
import glob

list_of_files = glob.glob('C:\\Users\Justin\Desktop\Datasets\Schrodinger Equation vs Real Experimental Data\small sample\*.png') # create the list of file
video_name = 'videoaaa.avi'


#frame = cv2.imread(os.path.join(image_folder, list_of_files[0]))
frame = cv2.imread(list_of_files[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 2, (width,height))
        
#for filePath in list_of_files:
#    video.write(cv2.imread(list_of_files))
    
for i in range(len(list_of_files)):
    video.write(cv2.imread(list_of_files[i]))
    print(list_of_files[i])
    
# For some reason the above is not working, it is ordering by first digit so 200 > 1000. Revise.

cv2.destroyAllWindows()
video.release()





"""
image_folder = 'C:\\Users\Justin\Desktop\Datasets\Schrodinger Equation vs Real Experimental Data\small sample'
video_name = 'videozzz.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
"""