
import os,sys
import numpy as np
import pandas as pd

import pickle

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from src.exception import CustomeException
from src.logr import logging


def save_obj(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomeException(e,sys)


def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(x_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(x_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomeException(e,sys)










