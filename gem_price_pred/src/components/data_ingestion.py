#  we are expecting the output from this script as train and test split data 

import os,sys
import pandas as pd

# importing our libs

from src.exception import CustomeException
from src.logr import logging


# for train test split
from sklearn.model_selection import train_test_split

# this lib is new and is used to replace constructor in a class. you can directly initialize the varibales using this lib
from dataclasses import dataclass 
# used as decorator above class


from src.components.data_transformation import DataTransformation

## initialize the data ingetion configuration


@dataclass
class DataIngestionconfig:

    # train data path
    # train_data_path:str=os.path.join("folder_path_for_data","train.csv")
    train_data_path:str=os.path.join(r"gem_price_pred\artifcats","train.csv")

    # test data path
    test_data_path:str=os.path.join(r"gem_price_pred\artifcats","test.csv")
    # rwa data path to keep it as a copy of main data
    rwa_data_path:str=os.path.join(r"gem_price_pred\artifcats","raw.csv")


## create a class for data ingestion

class DataIngestion:

    # we are now not using data classes for creating variable so we will use __init__ constructor

    def __init__(self):
        self.ingestion_config = DataIngestionconfig() # this will store all 3 path as tupel for train test and raw csv

    # now we will do the processing on the data
    def initiate_data_ingestion(self):
        logging.info("data ingestion method started")

        try:

            # get data fro  CSV/database u can craete function in utils file and call it here

            df=pd.read_csv(os.path.join(r'gem_price_pred\notebooks\data','gemstone.csv'))

            # df=pd.read_csv(os.path.join('notebooks\data','gemstone.csv'))
            logging.info("dataset reading as pandas data frame")

            #creating copy as raw data
            os.makedirs(os.path.dirname(self.ingestion_config.rwa_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.rwa_data_path, index=False)
            

            logging.info("initializing train test split")

            train_set, test_set = train_test_split(df, test_size=0.3,random_state=30)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info("ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) # at the end we return the data paths for both test and test for further pipeline

        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise CustomeException(e,sys)
            


 


""""
Test your code like this 


if __name__ == "__main__":
    obj = DataIngestion() # craete object of that class
    train_data_path, test_data_path =  obj.initiate_data_ingestion()

    data_transform = DataTransformation()
    train_arr,test_arr,_ = data_transform.initiate_data_transformation(train_data_path,test_data_path) # a pickel file is expected 

"""














