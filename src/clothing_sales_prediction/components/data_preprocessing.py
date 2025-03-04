from pathlib import Path  
import os 

import pandas as pd  
import numpy as np 

from clothing_sales_prediction import logger  
from clothing_sales_prediction.utils.common import get_size
from clothing_sales_prediction.entity.config_entity import DataPreprocessingConfig  

from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder

import joblib

class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def load_dataset(self):
        df = pd.read_csv(self.config.clothSalesDataset)
        return df
    
    def preprocessingDataset(self, df):
        # replace the column
        df['Sales'] = df.pop('Sales')

        # Discretization using numpy
        df['Sales'] = np.where(df['Sales'] > df['Sales'].median(), 1, 0)
        # get all the categorical columns
        categoryColumns = df.select_dtypes(include='object').columns
        # pipeline
        categoryPipeline = Pipeline([
            ('category', OneHotEncoder(drop='first'))
        ])
        # Column Transfer
        preprocess = ColumnTransformer([
            ('category', categoryPipeline, categoryColumns)
        ], remainder='passthrough')

        joblib.dump(preprocess, self.config.preprocessModel)

        if not os.path.exists(self.config.load_data):
            
            preprocess = joblib.load(self.config.preprocessModel)
            cleanDataset = pd.DataFrame(preprocess.fit_transform(df),  columns = preprocess.get_feature_names_out())
            cleanDataset.to_csv(self.config.load_data, index=False)
            logger.info(f"{self.config.load_data} successfully preprocessed. Saved as cleanDataset.csv")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.load_data))}")

       

    
