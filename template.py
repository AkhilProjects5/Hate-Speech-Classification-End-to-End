# Commonly used 

import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[%(ascii)s] : %(message)s:")   # Each time template.py is called it will print logs in console in the given format

project_name = "Hate_speech_classifier"  # Root folder name

list_of_files = [

    f"{project_name}/components/__init__.py",  #Local folder so need a constructor file inside
    f"{project_name}/components/data_ingestion.py" ,
    f"{project_name}/components/data_transformation.py" ,
    f"{project_name}/components/model_evaluation.py" ,
    f"{project_name}/components/model_trainer.py" ,
    f"{project_name}/components/model_pusher.py",   # Since models needs to be pushed to GCP

    f"{project_name}/configuration/__init__.py" ,
    f"{project_name}/configuration/google_cloud_sync.py", # Syncs local and cloud files
    

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/feature.py",
    f"{project_name}/ml/model.py" , # here RNN will be made and imported.


    "app.py", #main.py,
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"

]

for filepath in list_of_files:
    filepath = Path(filepath)

    direct , filename = os.path.split(filepath)

    if direct != "":
        os.makedirs(direct, exist_ok = True)
        logging.info(f"Creating directory ; {direct} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)  == 0 ):
        with open(filepath , "w") as f:
            pass
        logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists")