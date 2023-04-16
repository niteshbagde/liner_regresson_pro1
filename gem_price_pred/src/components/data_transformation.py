
"""
# this is for feature engineering 

we apply transformation ==> expected output is transfromed data and pipeline pickel files [saved in artifact folder]

expected operations: 

[handeling missing values , feature scaling , handeling categorical data , handeling numerical data , etc.]

"""


import pandas as pd
import os , sys
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# project libs
from src.exception import CustomeException
from src.logr import logging

from src.utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessors_obj_file_path = os.path.join(r"gem_price_pred\artifcats" , "processor.pkl")
    """
    A pickle file is a binary file format used to store and serialize Python objects, which can later be deserialized (i.e., read back into memory) by a Python program. Pickle files have the file extension .pkl or .pickle.

    The main purpose of using a pickle file is to save an object in a way that it can be easily retrieved and used later on without having to recreate it from scratch. This can be useful when working with large datasets, complex machine learning models, or any other object that takes a lot of time to create.

    To create a pickle file, you can use the pickle.dump() function in Python. This function takes two arguments: the object you want to pickle, and the file object you want to save the pickled object to.To load a pickle file back into memory, you can use the pickle.load() function.

    import pickle
    # Open a file and pickle the object to it
    with open("my_object.pkl", "wb") as f:
        pickle.dump(my_object, f)

    with open("my_object.pkl", "rb") as f:
        my_object = pickle.load(f)

    """


class DataTransformation:
    def __init__(self):
        self.data_transformation_obj = DataTransformationConfig()


    def get_data_transformation_object(self):

        try:
            logging.info("data transformation initiated")

            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable with respect to index position in list
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']



            logging.info('Pipeline Initiated')
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                        ('imputer',SimpleImputer(strategy='median')),
                        ('scaler',StandardScaler())
                        ]

                                )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )

            # column transform is method from sklearn
            preprocessor=ColumnTransformer([
            ('num_pipeline', num_pipeline, numerical_cols),
            ('cat_pipeline', cat_pipeline, categorical_cols)
            ])
            
            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:

            logging.info("Error observed while data transformation")
            raise CustomeException(e,sys)

        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            #read test train data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("reading completed for test train data as pandas dataframe")

            logging.info(f"Train dataframe head : \n {train_df.head(3).to_string()}")
            logging.info(f"Test dataframe head : \n {test_df.head(3).to_string()}")

            logging.info("obtaining preprocesing object")
            
            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = "price"

            drop_column = [target_column_name,"id"]

            # xtrain and ytrain
            input_feature_train_df = train_df.drop(columns = drop_column, axis = 1) # its like X or X_train
            target_feature_train_df = train_df[target_column_name] # and its like y or y_train

            # xtest and ytest
            input_feature_test_df = test_df.drop(columns = drop_column, axis = 1)  # X_test
            target_feature_test_df = test_df[target_column_name] # y_test

            # transforming usng preprocessing the object
            # for training model on x train -  input data to estimate the necessary parameters (such as mean, standard deviation, min, max) based on the training data
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)

            # for testing the model on x test
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            """
            In machine learning, both fit_transform() and transform() are methods used for feature engineering or data preprocessing.

            The fit_transform() method is used to learn the parameters from the training data and transform the training data into a new form using those parameters. In other words, this method is used to fit the preprocessing model to the training data and then transform the training data to create new features. The fit_transform() method is typically used only on the training data, and not on the test data.

            On the other hand, the transform() method is used to apply the same transformation that was learned from the training data to the test data. This method is used to transform the test data using the same preprocessing model that was fit on the training data. The transform() method is called on the test data after the model has been trained using the fit_transform() method.

            In summary, fit_transform() is used to fit the preprocessing model to the training data and transform the training data into a new form, while transform() is used to apply the same transformation to the test data that was learned from the training data.
            
            """

            logging.info("applying preprocessing object on training and testing dataset")

            train_arr = np.c_[input_feature_train_arr , np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            """
            np.c_ is a NumPy object used for concatenating 1-D arrays as columns to produce a 2-D array. It takes two or more 1-D arrays as input and returns a 2-D array by concatenating them along the second axis (column-wise).

            In the above code, np.c_ is used to concatenate the input_feature_train_arr and target_feature_train_df arrays column-wise to create a new 2-D array train_arr. Similarly, np.c_ is used to concatenate input_feature_test_df and target_feature_test_df arrays column-wise to create target_arr.
            """

            # save pickel file
            save_obj(

                file_path=self.data_transformation_obj.preprocessors_obj_file_path,
                obj=preprocessing_obj

            )
           
            logging.info("prepossing pickel file object saved successfully")

            return (
                train_arr,
                test_arr,
                self.data_transformation_obj.preprocessors_obj_file_path,
            )
            

            

        except Exception as e:
            logging.info("exception occured in the initate data transformation")
            raise CustomeException(e,sys)
