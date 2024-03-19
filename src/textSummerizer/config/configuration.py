# 4. configuration manager in src config.
# create constant in the constant folder->__init__py file

from textSummerizer.constants import *
from textSummerizer.utils.common import read_yaml, create_directories
from textSummerizer.entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig)



class ConfigurationManager:
    #constructor assigning values from constant file to the class variables
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # reading yaml config file and params file and assigning them to the class variables

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # create directories/file for artifacts
        # note that we are using . to access, as we have defined using confixbox

        create_directories([self.config.artifacts_root])

    # user defined functions with parameters returned type are based on the deorator function defined in above cell

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    # user defined functions with parameters returned type are based on the decorator function defined in above cell
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config



    # user defined functions with parameters returned type are based on the decorator function defined in above cell
    # returns the 3 variables
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir]) # create directories for data transformation

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config