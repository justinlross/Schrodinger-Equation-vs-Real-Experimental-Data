"""
This file contains all the code for processing the experimental data
including cleaning it and converting it into workable formats.

Author: Justin L Ross -
License: BSD


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


asciiFolder = 'C:\\Users\Justin\Desktop\Datasets\Ghost Imaging SM\*.asc'
pngFolder = 'C:\\Users\Justin\Desktop\Datasets\Ghost Imaging SM Contents\images\*.png'
csvFolder = 'C:\\Users\Justin\Desktop\Datasets\Schrodinger Equation vs Real Experimental Data\csvheraldedSM\*.csv'
videoFileName = 'videoaaazzzz.avi'


######################################################################
# Functions and Code


def convert_ascii_to_png(asciiFolder):
    lines = []
    collisionMatrix = np.array([])
    counter = 0
    list_of_files = glob.glob(asciiFolder) # create the list of file

    for filePath in list_of_files:
        with open(filePath,encoding="ascii") as dataInput:
            for line in dataInput:
                line = line.split()
                for item in line:
                    item = item.strip()
                    if item.isnumeric():
                        lines.append(int(item))

        collisionMatrix = np.append(collisionMatrix, [lines]) # perhaps use vertical stack here!!!
        grid = np.resize(collisionMatrix,(512, 512)) # 262144 produces 512 by 512
        grid = np.swapaxes(grid,0,1) # check to make sure this is the correct axis swap, probably a better way to do this.

        dfend = pd.DataFrame(grid)
    
        """
        Section for styling the plot.
        """
        # Style the plot
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(dfend, cmap=plt.cm.viridis, vmin=0, vmax=10)
        
        # The following is for getting rid of the white border.
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.box(on=None)
        plt.axis('off')

        #Viridis is chosen as it is a great colour map that is dark to light.
        fig.set_size_inches(14, 14)
    
    
        #This is for saving the file.
        saveName ='images/' + (str("%04d" % counter) + '.png')
        #plt.savefig(saveName,bbox_inches='tight',pad_inches = -1)
        #plt.savefig(saveName)
        plt.savefig(saveName,bbox_inches='tight',aspect='auto', pad_inches = -0)
        plt.close('all')

        #This is for clearning the stored data.
        collisionMatrix = np.array([]) # This is the line causing the issue, unclear why.
        dfend = np.array([])
        grid = np.array([])
        lines.clear()
        counter += 1
    return


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
        saveName ='csvghost/' + (str("%04d" % counter) + '.csv')
        dfend.to_csv(saveName)

        #This is for clearning the stored data.
        #collisionMatrix = np.empty([]) # This is the line causing the issue, unclear why.
        #dfend = np.empty([])
        #grid = np.empty([])
        
        
        collisionMatrix = np.array([]) # This is the line causing the issue, unclear why.
        dfend = np.array([])
        grid = np.array([])
        lines.clear()
        counter += 1
    return


"""
def convert_csv_to_png():
    lines = []
    collisionMatrix = np.array([])
    counter = 0
    list_of_files = glob.glob(csvFolder)
    
    for filePath in list_of_files:
        # with open(filePath,encoding="csv") as dataInput:
        # with open(filePath, newline='') as dataInput: # BLAH BLAH
        with open(filePath, header=None) as dataInput: # BLAH BLAH
            for line in dataInput:
                #print(line)
                line = line.split()
                print(line)
                for item in line:
                    item = item.strip()
                    if item.isnumeric():
                        lines.append(int(item))

        collisionMatrix = np.append(collisionMatrix, [lines]) # perhaps use vertical stack here!!!
        grid = np.resize(collisionMatrix,(512, 512)) # 262144 produces 512 by 512
        grid = np.swapaxes(grid,0,1) # check to make sure this is the correct axis swap, probably a better way to do this.

        dfend = pd.DataFrame(grid)
    
        # Style the plot
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(dfend, cmap=plt.cm.viridis, vmin=0, vmax=10)
        
        # The following is for getting rid of the white border.
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.box(on=None)
        plt.axis('off')

        #Viridis is chosen as it is a great colour map that is dark to light.
        fig.set_size_inches(14, 14)
    
    
        #This is for saving the file.
        saveName ='imagescsvheralded' + (str("%04d" % counter) + '.png')
        #plt.savefig(saveName,bbox_inches='tight',pad_inches = -1)
        #plt.savefig(saveName)
        plt.savefig(saveName,bbox_inches='tight',aspect='auto', pad_inches = -0)
        plt.close('all')

        #This is for clearning the stored data.
        collisionMatrix = np.array([]) # This is the line causing the issue, unclear why.
        dfend = np.array([])
        grid = np.array([])
        lines.clear()
        counter += 1
    return
"""

def convert_csv_to_png():
    lines = []
    collisionMatrix = np.array([])
    counter = 0
    list_of_files = glob.glob(csvFolder)
    
    for filePath in list_of_files:
        # with open(filePath,encoding="csv") as dataInput:
        # with open(filePath, newline='') as dataInput: # BLAH BLAH
        dfend = pd.read_csv(filePath, header=None) # BLAH BLAH
    
        """
        Section for styling the plot.
        """
        # Style the plot
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(dfend, cmap=plt.cm.viridis, vmin=0, vmax=10)
        
        # The following is for getting rid of the white border.
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.box(on=None)
        plt.axis('off')

        #Viridis is chosen as it is a great colour map that is dark to light.
        fig.set_size_inches(14, 14)
    
    
        #This is for saving the file.
        saveName ='imagescsvheralded' + (str("%04d" % counter) + '.png')
        #plt.savefig(saveName,bbox_inches='tight',pad_inches = -1)
        #plt.savefig(saveName)
        plt.savefig(saveName,bbox_inches='tight',aspect='auto', pad_inches = -0)
        plt.close('all')

        #This is for clearning the stored data.
        collisionMatrix = np.array([]) # This is the line causing the issue, unclear why.
        dfend = np.array([])
        grid = np.array([])
        lines.clear()
        counter += 1
    return


def ascii_to_png_display():
    
    lines = []
    rowVar = pd.Series()
    df = np.array([])

    filePath = r"C:\\Users\Justin\Desktop\Datasets\Ghost Imaging SM\4070.asc"


    with open(filePath,encoding="ascii") as dataInput:
        for line in dataInput:
            line = line.split()
            for item in line:
                item = item.strip()
                if item.isnumeric():
                    lines.append(int(item))

    df = np.append(df, [lines]) # perhaps use vertical stack here!!!
    grid = np.resize(df,(512, 512)) # 262144 produces 512 by 512
    grid = np.swapaxes(grid,0,1) # check to make sure this is the correct axis swap, probably a better way to do this.
    print(np.max(grid))
    dfend = pd.DataFrame(grid)

    # styling
    # Style the plot
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(dfend, cmap=plt.cm.viridis, vmin=0, vmax=78)
    #Viridis is chosen as it is a great colour map that is dark to light.
    fig.set_size_inches(14, 14)


    #ax.set_xticks(np.arange(0, 512, step=50))
    #ax.set_yticks(range(0,512,100))
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.box(on=None)
    plt.axis('off')
    plt.savefig("test.png",bbox_inches='tight',aspect='auto', pad_inches = -0)
    
    return


def create_video_from_png_files(pngFolder,videoFileName):
    list_of_files = glob.glob(pngFolder) # create the list of file
    
    frame = cv2.imread(list_of_files[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(videoFileName, 0, 2, (width,height))
        
    
    for i in range(len(list_of_files)):
        video.write(cv2.imread(list_of_files[i]))

    cv2.destroyAllWindows()
    video.release()
    return


######################################################################
"""
Uncomment whatever function you need to run.
"""


#convert_ascii_to_png(asciiFolder)
#convert_ascii_to_csv(asciiFolder)
convert_csv_to_png()
#create_video_from_png_files(pngFolder,videoFileName)
#ascii_to_png_display()