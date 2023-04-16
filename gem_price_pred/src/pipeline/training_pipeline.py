
from src.exception import CustomeException
import os, sys
from src.logr import logging
import pandas as pd
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
from src.components.model_trainier import ModelTrainer


if __name__ == "__main__":
    obj = DataIngestion() # craete object of that class
    train_data_path, test_data_path =  obj.initiate_data_ingestion()

    data_transform = DataTransformation()
    train_arr,test_arr,_ = data_transform.initiate_data_transformation(train_data_path,test_data_path) # a pickel file is expected 

    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)













