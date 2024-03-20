
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from textSummerizer.entity import ModelEvaluationConfig

# define the model evaluation class
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig): # initialize the model evaluation class
        self.config = config


    # define the method to generate batch sized chunks
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        """split the dataset into smaller batches that we can process simultaneously
        Yield successive batch-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size] # yield the batch sized chunks
        print("Batch sized chunks generated")

    # define the method to calculate the metric on the test dataset
    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer, 
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                               column_text="article", 
                               column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size)) # generate the article batches 
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size)) # generate the target batches
        
        # iterate through the article and target batches
        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):
            # tokenize the articles
            inputs = tokenizer(article_batch, max_length=1024,  truncation=True, 
                            padding="max_length", return_tensors="pt")
            # generate the summaries
            
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device), 
                            length_penalty=0.8, num_beams=8, max_length=128)
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''
            
            # Finally, we decode the generated texts, 
            # replace the  token, and add the decoded texts with the references to the metric.
            # decode the summaries
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=True) 
                for s in summaries]      
            # replace the empty strings with space
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            # add the decoded summaries to the metric
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        #  Finally compute and return the ROUGE scores.
        score = metric.compute()
        print("calculated score:",score)
        return score


    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {device}")
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        print(f"Tokenizer loaded from {self.config.tokenizer_path}")
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        print(f"Model loaded from {self.config.model_path}")
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        print(f"Dataset loaded from {self.config.data_path}")

        # define the rouge names
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        # load the rouge metric
        rouge_metric = load_metric('rouge')

        print("Calculating ROUGE on test dataset")

        score = self.calculate_metric_on_test_ds(
        dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, batch_size = 2, column_text = 'dialogue', column_summary= 'summary'
            )
        # create the dataframe
        rouge_dict = dict((rn, score[rn].mid.fmeasure ) for rn in rouge_names ) # create the rouge dictionary

        df = pd.DataFrame(rouge_dict, index = ['pegasus'] )
        print(df)
        df.to_csv(self.config.metric_file_name, index=False)

        print(f"ROUGE scores saved to {self.config.metric_file_name}")