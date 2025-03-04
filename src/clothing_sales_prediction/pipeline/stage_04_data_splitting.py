# Data splitting
import warnings  

from clothing_sales_prediction.config.configuration import ConfigurationManager
from clothing_sales_prediction.components.data_splitting import DataSplitting 
from clothing_sales_prediction import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data Splitting stage"

class DataSplittingTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_splitting_config = config.get_data_splitting_config()
        data_splitting = DataSplitting(config = data_splitting_config)
        df = data_splitting.load_Data()
        data_splitting.train_test_spiting(df)
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataSplittingTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    