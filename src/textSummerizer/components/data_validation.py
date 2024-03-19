

import os
from textSummerizer.logging import logger
from textSummerizer.entity import  DataValidationConfig

# create class for data validation component will use the class configuration manager

class DataValidation:

    # will take in the config object and will use the class configuration manager to get the data validation config object
    def __init__(self, config: DataValidationConfig):
        self.config = config # initialize the config object


    # method to validate all required files are present
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}") # Validation status will return false if any of the required files are not present
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e