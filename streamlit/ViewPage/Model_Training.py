import streamlit as st 

st.title("🧠 Model Training")

st.subheader("📌 Importing Libraries")
st.code(
    """import os 
import pandas as pd
from clothing_sales_prediction import logger
from clothing_sales_prediction.entity.config_entity import ModelTrainerConfig
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib""",
    language="python",
)

st.subheader("🛠️ Model Trainer Class")
st.code(
    """class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config""",
    language="python",
)

st.subheader("📥 Loading Data")
st.code(
    """def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]""",
    language="python",
)

st.subheader("🌳 Training Decision Tree")
st.code(
    """modelDT = DecisionTreeClassifier(
            criterion = self.config.DTParams['criterion'],
            max_depth = self.config.DTParams['max_depth'], 
            min_samples_split = self.config.DTParams['min_samples_split'], 
            min_samples_leaf = self.config.DTParams['min_samples_leaf'],
            random_state = self.config.DTParams['random_state']
        )

        modelDT.fit(train_x, train_y)
        joblib.dump(modelDT, self.config.DecisionTree)
        logger.info("Decision Tree model successfully built.")""",
    language="python",
)

st.subheader("🌲 Training Random Forest")
st.code(
    """modelRF = RandomForestClassifier(
            max_depth =  self.config.RFParams['max_depth'], 
            min_samples_split = self.config.RFParams['min_samples_split'], 
            min_samples_leaf = self.config.RFParams['min_samples_leaf'],
            n_estimators = self.config.RFParams['n_estimators'], 
            random_state = self.config.RFParams['random_state']
        )

        modelRF.fit(train_x, train_y)  
        joblib.dump(modelRF, self.config.RandomForest)
        logger.info("Random Forest model successfully built.")""",
    language="python",
)

st.write("✅ Models are successfully trained and saved!")
