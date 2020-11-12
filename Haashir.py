# %%
#import libraries 
import pandas as pd 
import numpy as np

# class proj():
#     def __init__(self, path_to_data) -> None:
#         self.data = self.readdata(path_to_data)

#     def readdata(self, path_to_data:str)-> pd.DataFrame:
#         """Load data from .csv or .xls or .xlsx file and return a Pandas data frame

#         Args:
#             path_to_data (str): full path to the data

#         Raises:
#             ValueError: If the file format is not .csv, .xls, .xlsx

#         Returns:
#             pd.DataFrame: data
#         """
#         if path_to_data.endswith('.csv'):
#             return pd.read_csv(path_to_data)
#         elif path_to_data.endswith('.xls') or path_to_data.endswith('.xlsx'):
#             return pd.read_excel(path_to_data)
#         else:
#             raise ValueError("Unknown file format, need .csv or .xlsx, you provided: {}"\
#                 .format( os.path.split(path_to_data)[1] ))

#     def create_train_test_split(self):
#         """Load data from .csv or .xls or .xlsx file and return a Pandas data frame

#         Args:
#             path_to_data (str): full path to the data

#         Raises:
#             ValueError: If the file format is not .csv, .xls, .xlsx

#         Returns:
#             pd.DataFrame: data
#         """
#         self.trX, self.trY, self.tsX, self.tsY = train_test_split(self.data, test_size=0.2, random_seed=42)

#     def create_model(self):
#         self.model = sklearn.rf() # pass in the right args

#     def fit_model(self):
#         self.model.fit(self.trX, self.trY)
    
#     def infer(self):
#         self.preds = self.model.predict(self.tsX)
    
#     def calc_error(self):
#         self.err = self.calculate_error(self.tsY, self.preds)

# pred_model = proj('abc.xlsx') # create object and load data
# pred_model.create_train_test_split()
# pred_model.create_model()
# pred_model.fit_model()
# pred_model.infer()
# pred_model.calc_error()
# pred_model.create_plots()
# pred_model.print_results()


# def add_sk(a:int,  b:int) -> int:
#     """Adds two integers and returns an integer

#     Args:
#         a (int): 1st integer
#         b (int): 2nd integer

#     Returns:
#         int: Result of sum
    
#     Raises:
#         AssertionError: if a or b is not an int
#     """
#     assert isinstance(a, int), "a (1st arg) type must be integer, you provided: {}".format(type(a))
#     assert isinstance(b, int), "b (2nd arg) type must be integer, you provided: {}".format(type(b))
#     return a+b

# print( add_sk(2,3) )