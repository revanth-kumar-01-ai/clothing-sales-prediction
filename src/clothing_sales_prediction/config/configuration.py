# configuration manager in src config
import warnings 

from clothing_sales_prediction.constants import *
from clothing_sales_prediction.utils.common import read_yaml, create_directories 
from clothing_sales_prediction.entity.config_entity import (DataIngestionConfig, DataPreprocessingConfig, DataValidationConfig, DataSplittingConfig, ModelTrainerConfig, ModelEvaluationConfig)

warnings.filterwarnings('ignore')

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):


        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)


        create_directories([self.config.artifacts_root])

    # data ingestion 💉
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion


        create_directories([config.root_dir])


        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_query=config.source_query,
            load_data=config.load_data,
        )


        return data_ingestion_config

    # data preprocessing 
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing

        create_directories([config.root_dir])

        data_preprocess_config = DataPreprocessingConfig(
            root_dir=config.root_dir,
            clothSalesDataset=config.clothSalesDataset,
            load_data=config.load_data,
            preprocessModel=config.preprocessModel
        )

        return data_preprocess_config

    # Data Validation 
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS


        create_directories([config.root_dir])


        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            cleanDataset = config.cleanDataset,
            all_schema=schema,
        )

        return data_validation_config
    
    # Data Splitting  
    def get_data_splitting_config(self) -> DataSplittingConfig:
        
        config = self.config.data_splitting

        create_directories([config.root_dir])

        data_splitting_config = DataSplittingConfig(
            root_dir=config.root_dir, 
            cleanData=config.cleanData,
            testData=config.testData, 
            trainData=config.trainData
        )

        return data_splitting_config
    
    # model training 
    def get_model_training(self) -> ModelTrainerConfig:
        
        config = self.config.model_trainer
        DecisionTreeParams = self.params.DecisionTree
        RandomForestParams = self.params.RandomForest
        target = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path, 
            DecisionTree = config.DecisionTree,  # model path don't confuse 
            RandomForest= config.RandomForest,   # model path don't confuse 
            DTParams = DecisionTreeParams, # this params 
            RFParams = RandomForestParams, # this params
            target_column = target.name
        )

        return model_trainer_config
    
    # Evaluation 
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        DFParams = self.params.DecisionTree
        RFParams = self.params.RandomForest
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            DecisionTreeModel = config.DecisionTreeModel,
            RandomForestModel = config.RandomForestModel,
            DFParams = DFParams,
            RFParams = RFParams,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/revanth-kumar-01-ai/clothing-sales-prediction.mlflow",
           
        )


        return model_evaluation_config
    
