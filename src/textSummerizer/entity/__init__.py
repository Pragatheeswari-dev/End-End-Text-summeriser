#  3. entity - define the return type of the function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen  = True) # define the custom return type of the function - decorator function
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path