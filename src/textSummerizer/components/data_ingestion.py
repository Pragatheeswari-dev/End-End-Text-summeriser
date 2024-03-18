
import os
import urllib.request as request # download and unzip files
import zipfile
from textSummerizer.logging import logger # custom logger
from textSummerizer.utils.common import get_size # get size module from utils.common
from pathlib import Path
from textSummerizer.entity import DataIngestionConfig

# create class for data ingestion component will use the class configuration manager
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 
        # assign config to the class variable and intialize instance variable


    # download and unzip files from source URL(defined  in the config.yaml) to local data file 
    # logging the download progress in the logger and return the size of the downloaded file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    # unzip files from local data file to unzip_dir
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


    