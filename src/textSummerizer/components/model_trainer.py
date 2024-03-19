
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
import os
from textSummerizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig): # initialize the model with the given config
        self.config = config


    # train the model
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu" # select the device to train on gpu or cpu
        print("device: ", device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) # initialize the tokenizer with the model checkpoint
        print("tokenizer: completed")


        print("self.config.model_ckpt",self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device) # initialize the model with the model checkpoint
        print("model_pegasus loaded")

        
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus) # initialize the data collator with the tokenizer and model checkpoint for the batches
        print("seq2seq_data_collator completed ")
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        print("dataset_samsum_pt completed ")

        print("output_dir=", self.config.root_dir,
            "num_train_epochs=", type(self.config.num_train_epochs), 
            "warmup_steps=", type(self.config.warmup_steps),
            "per_device_train_batch_size=",  type(self.config.per_device_train_batch_size), 
            "per_device_eval_batch_size=", type(self.config.per_device_train_batch_size),
            "weight_decay=",type(self.config.weight_decay), 
            "logging_steps=",type(self.config.logging_steps),
            "evaluation_strategy=",type(self.config.evaluation_strategy), 
            "eval_steps=",type(self.config.eval_steps), 
            "save_steps=",type(self.config.save_steps), 
            "gradient_accumulation_steps=", type(self.config.gradient_accumulation_steps))

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=self.config.per_device_train_batch_size, 
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, 
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        ) 

     
        
        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"], 
                  eval_dataset=dataset_samsum_pt["validation"])

          
        print("training started: ")
        trainer.train()
        print("training completed: ")

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        print("model saved")
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
        print("tokenizer saved")