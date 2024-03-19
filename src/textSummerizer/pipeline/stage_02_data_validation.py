
from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.data_validation import DataValidation
from textSummerizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager() # initialize the class configuration manager
        data_validation_config = config.get_data_validation_config() # assign config to the class variable
        data_validation = DataValidation(config=data_validation_config) # initialize the class data validation component
        data_validation.validate_all_files_exist() # validate all required files are present