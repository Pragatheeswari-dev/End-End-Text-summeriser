#  3. entity - define the return type of the function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen  = True) # define the custom return type of the function - decorator function
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# 3. define the entity  for  DataIngestionConfig


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

# 3. define the entity for DataTransformationConfig


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path # root directory for data transformation
    data_path: Path # path to the original data used for data transformation
    tokenizer_name: Path # path to the tokenizer used for data transformation, model will be automatically downloaded.


# 3. define the entity for Model Training

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path # default path to the root directory
    data_path: Path # default path to the data directory
    model_ckpt: Path # default path to the model checkpoint directory
    num_train_epochs: int # default number of training epochs
    warmup_steps: int # default number of warmup steps
    per_device_train_batch_size: int # default batch size per device during training
    weight_decay: float # default weight decay coefficient
    logging_steps: int # default number of steps between logging training status
    evaluation_strategy: str # default evaluation strategy for evaluation
    eval_steps: int # default number of steps between evaluation
    save_steps: float # default number of steps between saving checkpoints
    gradient_accumulation_steps: int # default number of steps between gradient accumulation


# 3. define the entity for Model Evaluation
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path # root directory of the project
    data_path: Path # path to the data
    model_path: Path # path to the model
    tokenizer_path: Path # path to the tokenizer
    metric_file_name: Path # path to the metric file