
from textSummerizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

# Class to predict the summary of the given text
class PredictionPipeline:
    # Constructor to initialize the configuration
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config() # Get the configuration


    # Method to predict the summary of the given text
    def predict(self,text):
        # Load the tokenizer from the configuration 
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path) 

        # Set the generation parameters for the model to predict the summary
        # length_penalty: The parameter for controlling the length of the output
        # num_beams: The number of beams to use for the beam search
        # max_length: The maximum length of the output
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        # Load the model from the configuration and predict the summary
        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        # Predict the summary
        output = pipe(text, **gen_kwargs)[0]["summary_text"] # Get the summary text
        print("\nModel Summary:")
        print(output)

        return output