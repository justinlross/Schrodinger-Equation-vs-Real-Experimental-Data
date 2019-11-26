# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:51:52 2019

Author: Justin L Ross -
License: BSD

This section contains all the code for processing the experimental data
including cleaning it and converting it into workable formats.
"""

######################################################################
# Load libraries

# default imported data science libraries
import numpy as np;
import pandas as pd;
import matplotlib as mpl;
import matplotlib.pyplot as plt;

# expanded imported libraries
import csv # For working with csv files
import glob # For collecting files together
import cv2 # For the video file


######################################################################
# Declare variables and constants


asciiFolder = 'C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\*.asc'
pngFolder = 'C:\\Users\Justin\Desktop\Datasets\Schrodinger Equation vs Real Experimental Data\images\*.png'



######################################################################

def convert_ascii_to_png(asciiFolder):
    
    return


asciiFolder = 'C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\*.asc'


def convert_ascii_to_csv(asciiFolder):
    lines = []
    collisionMatrix = np.array([])
    counter = 0
    list_of_files = glob.glob(asciiFolder)

    for filePath in list_of_files:
        with open(filePath,encoding="ascii") as dataInput:
            for line in dataInput:
                line = line.split()
                for item in line:
                    item = item.strip()
                    if item.isnumeric():
                        item = int(item)
                        lines.append(item)

    collisionMatrix = np.append(collisionMatrix, [lines]) # perhaps use vertical stack here!!!
    grid = np.resize(collisionMatrix,(512, 512)) # 262144 produces 512 by 512
    grid = np.swapaxes(grid,0,1) # check to make sure this is the correct axis swap, probably a better way to do this.

    dfend = pd.DataFrame(grid)
        
    
    #This is for saving the file.
    saveName ='csv/' + (str("%04d" % counter) + '.csv')
    dfend.to_csv(saveName)

    #This is for clearning the stored data.
    collisionMatrix = np.empty([]) # This is the line causing the issue, unclear why.
    dfend = np.empty([])
    grid = np.empty([])
    lines.clear()
    counter += 1
    
    return



def create_video_from_png_files(pngFolder):
    list_of_files = glob.glob(pngFolder) # create the list of file
    video_name = 'videoaaa.avi'
    
    frame = cv2.imread(list_of_files[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 2, (width,height))
        
    
    for i in range(len(list_of_files)):
        video.write(cv2.imread(list_of_files[i]))

    cv2.destroyAllWindows()
    video.release()
    
    return


######################################################################
    

