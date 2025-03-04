# model Evaluation
import warnings  

from clothing_sales_prediction.config.configuration import ConfigurationManager
from clothing_sales_prediction.components.modelEvaluation import ModelEvaluation
from clothing_sales_prediction import logger


warnings.filterwarnings('ignore')

STAGE_NAME = "Data Model Evaluation Stage"


class ModelEvalPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_decision_tree_to_mlflow()
        model_evaluation_config.log_random_forest_tree_to_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvalPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e