# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:15:53 2019

@author: Justin
"""

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
            line = line.split()
            for item in line:
                item = item.strip()
                if item.isnumeric():
                    lines.append(int(item))

    df = np.append(df, [lines]) # perhaps use vertical stack here!!!
    grid = np.resize(df,(512, 512)) # 262144 produces 512 by 512
    grid = np.swapaxes(grid,0,1) # check to make sure this is the correct axis swap, probably a better way to do this.

    dfend = pd.DataFrame(grid)
        
    
    #This is for saving the file.
    saveName ='csv/' + (str("%04d" % counter) + '.csv')
    dfend.to_csv(saveName)

    #This is for clearning the stored data.
    df = np.empty([])
    dfend = np.empty([])
    grid = np.empty([])
    lines.clear()
    counter += 1
