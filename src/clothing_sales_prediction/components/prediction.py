#  prediction 
import joblib

from clothing_sales_prediction import logger  
from clothing_sales_prediction.entity.config_entity import ModelPredictionConfig  


class ForeCast:
    def __init__(self, config: ModelPredictionConfig):
        self.config = config

    def best_model_prediction(self, data):
    
        """
        Random Forest is used because it provides the best accuracy. If Decision Tree achieves better accuracy in the future, 
        we will use **self.config.DecisionTreeModel** instead.
        """
        
        model = joblib.load(self.config.RandomForestModel)
        predictionValue = model.predict([data])
        logger.info(f"Prediction successful: \033[92m{int(predictionValue)}\033[0m")
        return predictionValue
        