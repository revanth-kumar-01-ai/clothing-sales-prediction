import warnings 


from clothing_sales_prediction.config.configuration import ConfigurationManager
from clothing_sales_prediction.components.data_preprocessing import DataPreprocessing 
from clothing_sales_prediction import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data preprocessing stage"

class DataPreprocessingTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config = data_preprocessing_config)
        df = data_preprocessing.load_dataset()
        data_preprocessing.preprocessingDataset(df)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreprocessingTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e