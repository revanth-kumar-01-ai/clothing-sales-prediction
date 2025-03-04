from dataclasses import dataclass 
from pathlib import Path 

# data ingestion 💉
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_query: str  
    load_data: Path


# data preprocessing 
@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    clothSalesDataset: Path
    load_data: Path
    preprocessModel: Path


# data validation 
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    cleanDataset: Path
    all_schema: dict
