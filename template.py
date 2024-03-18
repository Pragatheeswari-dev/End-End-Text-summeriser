# python version v2024.2.1
import os
from  pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format= '[%(asctime)s]: %(message)s:')

#project folder structure
project_name = "textSummerizer"

#.github for CI/CD deployments - to hold yaml files and automaitically updates on the CI/CD deployments
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # __init__.py is contructor file, for installation  of local packages.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.yaml",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb"
]



for filepath in list_of_files:
    filepath = Path(filepath) #filepath is a pathlib.Path object and provides the full path to the file. Either windows or linux path
    filedir,filename = os.path.split(filepath) #split filepath and directory

    if filedir != "": # if directory does not exist, create it
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # file empty replaces or creates the file if it doesn't exist
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
            logging.info(f"File: {filepath} already exists")

