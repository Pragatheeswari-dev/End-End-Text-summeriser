from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.data_transformation import DataTransformation
from textSummerizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # initialize the class configuration manager
        data_transformation_config = config.get_data_transformation_config() # assign config to the class variable
        data_transformation = DataTransformation(config=data_transformation_config) # initialize the class data transformation component
        data_transformation.convert() # convert the data from disk to a pytorch dataset