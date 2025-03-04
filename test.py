import warnings
import pandas as pd
from clothing_sales_prediction.pipeline.state_07_prediction import ModelPrediction
from clothing_sales_prediction import logger

warnings.filterwarnings('ignore')

category__ShelveLoc_Good = 0.0
category__ShelveLoc_Medium = 1.0
category__Urban_Yes = 1.0
category__US_Yes = 1.0
remainder__CompPrice = 143.0
remainder__Income = 77.0
remainder__Advertising = 25.0
remainder__Population = 448.0
remainder__Price = 156.0
remainder__Age = 43.0
remainder__Education = 17.0

values = [
    category__ShelveLoc_Good, category__ShelveLoc_Medium, category__Urban_Yes, category__US_Yes,
    remainder__CompPrice, remainder__Income, remainder__Advertising, remainder__Population,
    remainder__Price, remainder__Age, remainder__Education
]

STAGE_NAME = "Prediction Stage"


try:
    predictor = ModelPrediction
    predictor.predict(values)  
except Exception as e:
    logger.error(f"Error during prediction: {e}")



