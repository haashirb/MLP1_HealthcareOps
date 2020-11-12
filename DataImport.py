# Author: Mohammed Haashir Butt

# IMPORTING LIBRARIES
import pandas as pd
import numpy as np

# FUNCTION: DataImport.py
def DataImport(Set):
    # LOADING IN FACILITY SHEETS
    if Set == '1':
        # read excel sheet 1 (facility 1)
        df = pd.read_excel('WalkInDataF1.xlsx')
    elif Set == '2':
        # read excel sheet 2 (facility 2)
        df = pd.read_excel('WalkInDataF2.xlsx')
    elif Set == '3':
        # read excel sheet 3 (facility 3)
        df = pd.read_excel('WalkInDataF3.xlsx')
    elif Set == '4':
        # read excel sheet 4 (facility 4)
        df = pd.read_excel('WalkInDataF4.xlsx')
    else:
        print("Invalid Set value. Select from 1, 2, 3, or 4.")

    # DROP ROW WITH ZEROS IN ALL COLUMNS
    null = df[df.isnull().any(axis=1)]
    indexToRemove = null.index
    df = df.drop(indexToRemove, axis=0)

    # DELETE ANONYMOUS DATA COLUMNS ("X_...")
    df = df.drop(df.columns[[1, 2, 3]], axis=1)

    # SAVING CLEANED DATA AS .pkl + commented code to print if you need to check pkl file created
    file_name = f"Data_{Set}.pkl"
    df.to_pickle(file_name)
    #print(pd.read_pickle('Data_4.pkl'))





