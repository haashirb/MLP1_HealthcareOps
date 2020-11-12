# Author: Mohammed Haashir Butt

# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
from statistics import stdev
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

    bFullEvaluation = False
    global TrainX
    global TrainY
    global fRemove

# FUNCTION: ComputeModel.py
def ComputeModel(DataX, DataY, nModel):

    # number of optimizing iterations
    if bFullEvaluation:
        NumEvals = 500
    else:
        NumEvals = 40


    # create training and test sets
    testFraction = ((0.2) + ((0.1) * random()))




    train_features, test_features, train_labels, test_labels =
    train_test_split(features, labels)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # nModel == 130 (Linear Regression)
    # nModel == 100 (MostRecentWait)

# FUNCTION: ComputeErrors
def ComputeErrors(YPredicted, Y):

    Residual = YPredicted - Y;


    from sklearn.metrics import r2_score
    coefficient_of_dermination = r2_score(y, p(x))



