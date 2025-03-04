import os 
import pandas as pd

from clothing_sales_prediction import logger
from clothing_sales_prediction.entity.config_entity import ModelTrainerConfig

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # decision tree 
        modelDT = DecisionTreeClassifier(
            criterion = self.config.DTParams['criterion'],
            max_depth = self.config.DTParams['max_depth'], 
            min_samples_split = self.config.DTParams['min_samples_split'], 
            min_samples_leaf = self.config.DTParams['min_samples_leaf'],
            random_state = self.config.DTParams['random_state']
        )

        modelDT.fit(train_x, train_y)
        joblib.dump(modelDT, self.config.DecisionTree)
        logger.info("Decision Tree model successfully built.")

        # Random Fores 
        modelRF = RandomForestClassifier(
            max_depth =  self.config.RFParams['max_depth'], 
            min_samples_split = self.config.RFParams['min_samples_split'], 
            min_samples_leaf = self.config.RFParams['min_samples_leaf'],
            n_estimators = self.config.RFParams['n_estimators'], 
            random_state = self.config.RFParams['random_state']
        )

        modelRF.fit(train_x, train_y)  
        joblib.dump(modelRF, self.config.RandomForest)
        logger.info("Random Forest model successfully built.")
        