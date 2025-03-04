# model Evaluation
import warnings  

from clothing_sales_prediction.config.configuration import ConfigurationManager
from clothing_sales_prediction.components.prediction import ForeCast

warnings.filterwarnings('ignore')


class ModelPrediction:
    def __init__(self):
        pass

    def predict(data):
        config = ConfigurationManager()
        model_prediction_config = config.get_model_prediction()
        model_prediction = ForeCast(config=model_prediction_config)
        model_prediction.best_model_prediction(data)

