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

