
from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.data_ingestion import DataIngestion
from textSummerizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager() # initialize the class configuration manager
        data_ingestion_config = config.get_data_ingestion_config() # assign config to the class variable
        data_ingestion = DataIngestion(config=data_ingestion_config) # initialize the class data ingestion component
        data_ingestion.download_file() # download and unzip files from source URL(defined  in the config.yaml) to local data
        data_ingestion.extract_zip_file()  # unzip files from local data file to unzip_dir
