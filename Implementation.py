# Author: Mohammed Haashir Butt
# Project Implementation File

import pandas as pd 
import numpy as np 

class HealthcareProj(): 
    """Creating a class for the Healthcare Operations managementproject
    """
    def __init__(self, path_to_data) -> None:
        self.data = self.readdata(path_to_data)

    def readdata(self, path_to_data:str) -> pd.DataFrame:
        """Load data from .xlsx, .xls, .csv file for one single facility, clean it, and return it as a dataframe

        Args:
            path_to_data (str): [description]

        Raises:
            ValueError: If file format is not .xlsx

        Returns:
            pd.DataFrame: [description]
        """

        # conditions for file: 
        # if .xlsx, do cleaning and save as d
        # if not, raise ValueError prompting user to use correct file format 

        if path_to_data.endswith('.xlsx') or path_to_data.endswith('.xls'):

            # read in file and save into dataframe
            df = pd.read_excel(path_to_data)

            # drop rows with zeros in all columns (if any)
            null = df[df.isnull().any(axis=1)]
            indexToRemove = null.index
            df = df.drop(indexToRemove, axis=0)

            # delete anonymized data columns ("X_...")
            df = df.drop(df.columns[[1, 2, 3]], axis=1)

            # return dataframe
            return(df)

        elif path_to_data.endswith('.csv'):

            # read in file and save into dataframe
            df = pd.read_csv(path_to_data)

            # drop rows with zeros in all columns (if any)
            null = df[df.isnull().any(axis=1)]
            indexToRemove = null.index
            df = df.drop(indexToRemove, axis=0)

            # delete anonymized data columns ("X_...")
            df = df.drop(df.columns[[1, 2, 3]], axis=1)

            # return dataframe
            return(df)

        else: 

            # raise an error if the extension of the file provided is incorrect
            raise ValueError("Path leads to a file that is not in .xlsx, .xls, or .csv format. You provided: {}"\
                .format(os.path.split(path_to_data)[1]))
        