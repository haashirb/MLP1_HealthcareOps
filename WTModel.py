# Author: Mohammed Haashir Butt

# IMPORTING LIBRARIES
from DataImport import DataImport
import pandas as pd
import numpy as np
from statistics import stdev

#def WTModel():
    # globals
    # ask user to input the modality for the correct facility (can include error condition later)

modality = int(input("Enter facility number (1,2,3, or 4): "))

if modality == 1:
    DataImport('1')
    df = pd.read_pickle('Data_1.pkl')
    #print(df)
elif modality == 2:
    DataImport('2')
    df = pd.read_pickle('Data_2.pkl')
    #print(df)
elif modality == 3:
    DataImport('3')
    df = pd.read_pickle('Data_3.pkl')
    #print(df)
elif modality == 4:
    DataImport('4')
    df = pd.read_pickle('Data_4.pkl')
    #print(df)
else:
    print("Error: Couldn't read pkl file. Please enter either 1, 2, 3, or 4 for the facility number.")

DataY = df.iloc[:, [0]]
DataX = df.iloc[:, 1:]
#print(DataX)







