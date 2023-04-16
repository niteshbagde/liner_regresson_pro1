import os, sys

from src.logr import logging
from src.exception import CustomeException

import pandas as pd

from src.utils import load_obj



class PredictionPipeline:

    def __init__(self) -> None:
        
        pass

    def predict(self,features):

        try:
            preprocessor_path = os.path.join(r"gem_price_pred\artifcats","processor.pkl")

            model_path = os.path.join(r"gem_price_pred\artifcats","Model.pkl")

            preprocessor = load_obj(preprocessor_path)

            model = load_obj(model_path)

            data_scale = preprocessor.transform(features)

            pred = model.predict(data_scale)

            return pred
        
        
        
        except Exception as e:
            logging.info("error occured while model prediction")
            raise CustomeException(e,sys)
        
        
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
        
    def get_data_as_dataframe(self):
        try:

            # create dictonary
            custom_data_input_dic = {

                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]

            }

            # read dictonary as datafram using pandas

            df = pd.DataFrame(custom_data_input_dic)
            logging.info("data gathered . inputs converted to dataframe")

            return df

        except Exception as e:
            logging.info("exception occured in prediction pipeline")
            raise CustomeException(e,sys)
        







