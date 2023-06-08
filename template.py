import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/conponents/data_ingestion.py",
    f"src/{project_name}/conponents/data_transformation.py",
    f"src/{project_name}/conponents/data_validation.py",
    f"src/{project_name}/conponents/model_evaluation.py",
    f"src/{project_name}/conponents/model_trainer.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    # make sure the file is compatible with every platform (windows, linux, mac)
    filepath = Path(filepath)
    # spliting the folder and the filename separately                          
    filedir, filename = os.path.split(filepath)   
    
          
    # make sure the file is not empty 
    if filedir != "":    
        # make directory if not exists                                
        os.makedirs(filedir, exist_ok=True) 
        # saving the log information            
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # creating the file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")