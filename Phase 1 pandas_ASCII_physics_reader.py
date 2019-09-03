# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:37:59 2019

@author: Justin L Ross
"""

# default imported data science libraries
import numpy as np;
import pandas as pd;
import matplotlib as mpl;
import matplotlib.pyplot as plt;

# expanded imported libraries
import csv
import glob

# importing data

# The file is encoded as ascii and we have chosen this error method handling as it is the strictest.
#ds = open(r"C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc",encoding="ascii", errors="surrogateescape")
#dataInput = ds.read()
lines = []
df = np.array([])
counter = 0
#df = pd.DataFrame()
#df = pd.DataFrame(index=range(512),columns=range(512))
list_of_files = glob.glob('C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\*.asc') # create the list of file
#list_of_files = glob.glob('C:\\Users\Justin\Desktop\Datasets\S Test Files\*.asc') # create the list of file

for filePath in list_of_files:
    with open(filePath,encoding="ascii") as dataInput:
        for line in dataInput:
            for item in line:
                if item.isnumeric():
                    lines.append(int(item))

    df = np.append(df, [lines]) # perhaps use vertical stack here!!!
    grid = np.resize(df,(512, 512)) # 262144 produces 512 by 512
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
    df = np.empty([])
    dfend = np.empty([])
    grid = np.empty([])
    lines.clear()
    counter += 1
