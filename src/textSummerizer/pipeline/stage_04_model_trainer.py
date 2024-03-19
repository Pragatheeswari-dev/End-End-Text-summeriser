
from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.model_trainer import ModelTrainer
from textSummerizer.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # initialize the configuration manager
        model_trainer_config = config.get_model_trainer_config() # get the model trainer config from the config file
        model_trainer_config = ModelTrainer(config=model_trainer_config) # initialize the model trainer with the model trainer config
        model_trainer_config.train() # train the model