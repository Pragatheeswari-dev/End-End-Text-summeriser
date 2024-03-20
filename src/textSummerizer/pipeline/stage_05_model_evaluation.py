
from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.model_evaluation import ModelEvaluation
from textSummerizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # initialize the configuration manager
        model_evaluation_config = config.get_model_evaluation_config() # get the model evaluation config
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config) # create the model evaluation class
        model_evaluation_config.evaluate() # evaluate the model