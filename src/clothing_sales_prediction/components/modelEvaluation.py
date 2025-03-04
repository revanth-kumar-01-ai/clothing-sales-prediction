import warnings 
from pathlib import Path
import os
import pandas as pd

from clothing_sales_prediction.utils.common import save_json
from clothing_sales_prediction.entity.config_entity import ModelEvaluationConfig
from clothing_sales_prediction import logger

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import dagshub
import mlflow
from datetime import datetime

import joblib 

warnings.filterwarnings('ignore')

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self, actual, pred):

        # accuracy 
        acc = accuracy_score(y_pred = pred, y_true = actual)

        # precision
        precision = precision_score(y_pred = pred, y_true = actual)

        # recall
        recall = recall_score(y_pred = pred, y_true = actual)

        # f1 score
        f1 = f1_score(y_pred = pred, y_true = actual)
        return acc, precision, recall, f1
    


    def log_decision_tree_to_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        modelDT = joblib.load(self.config.DecisionTreeModel)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Dagshub
        dagshub.init(repo_owner='revanth-kumar-01-ai', repo_name='clothing-sales-prediction', mlflow=True)

        # run name
        run_name = f"DecisionTree_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        mlflow.set_experiment('DecisionTree_Experiment') # Experiment Name
        with mlflow.start_run():
            predicted_qualities = modelDT.predict(test_x)
            (acc, precision, recall, f1) = self.eval_metrics(test_y, predicted_qualities)
            scores = {"accuracy_score": acc, "precision_score": precision, "recall_score": recall, "f1": f1}
            save_json(path=Path(os.path.join(self.config.metric_file_name, "DecisionTreeMetric.json")), data=scores)

            mlflow.log_params(self.config.DFParams)
            mlflow.log_metric("accuracy_score", acc)
            mlflow.log_metric("precision_score", precision)
            mlflow.log_metric("recall_score", recall)
            mlflow.log_metric("f1", f1)

            logger.info(f"MLflow run '{run_name}' successfully created.")


    def log_random_forest_tree_to_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        modelRF = joblib.load(self.config.RandomForestModel)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Dagshub
        dagshub.init(repo_owner='revanth-kumar-01-ai', repo_name='clothing-sales-prediction', mlflow=True)

        # run name
        run_name = f"RandomForest_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        mlflow.set_experiment('RandomForest_Experiment') # Experiment Name
        with mlflow.start_run():
            predicted_qualities = modelRF.predict(test_x)
            (acc, precision, recall, f1) = self.eval_metrics(test_y, predicted_qualities) 
            scores = {"accuracy_score": acc, "precision_score": precision, "recall_score": recall, "f1": f1}
            save_json(path=Path(os.path.join(self.config.metric_file_name, "RandomForest.json")), data=scores)
        
            mlflow.log_params(self.config.DFParams)
            mlflow.log_metric("accuracy_score", acc)
            mlflow.log_metric("precision_score", precision)
            mlflow.log_metric("recall_score", recall)
            mlflow.log_metric("f1", f1)

            logger.info(f"MLflow run '{run_name}' successfully created.")

