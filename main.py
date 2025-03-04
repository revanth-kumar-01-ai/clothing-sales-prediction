from clothing_sales_prediction import logger 

from clothing_sales_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeLine
from clothing_sales_prediction.pipeline.stage_02_data_preprocessing import DataPreprocessingTrainingPipeLine

"""
Data ingestion from the mySQL database     
"""

STAGE_NAME = "Data Ingestion Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


"""
Data preprocessing  
"""

STAGE_NAME = "Data Preprocess Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataPreprocessingTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
