import os
import yaml
from src.DataScienceProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns
    
    Args:
        path_to_yaml(str): path to the yaml file like input
    Raises:
        ValueError if yaml file is empty

    Returns:
       ConfigBox: ConfigBox Type

    """
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f'Yaml File: {path_to_yaml} loaded successfully!')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'Yaml file {path_to_yaml} is empty!')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Create multiple directories
    
        Args:
        path_to_directories (list): List of paths to create
        verbose (bool): Whether to log each creation. Default is True.
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")
    
@ensure_annotations
def save_json(path:Path,data:dict):
    """save the JSON Data
    Args:
        path(Path): path to json file
        data(dict): Data to be saved in JSON File
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f'json file saved at: {path}') 

@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    """load the JOSN files data
    Args:
        path(Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f'json file loaded successfully from : {path}')
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save the binary file:
    Args:
        data(Any): Data to be saved as a binary file
        path(Path): Path to binary file


        Load binary data from a file
    Returns:
        Any: The deserialized Python object
    

    """
    joblib.dump(value=data,filename=path)
    logger.info(f'binary file saved at : {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path(Path): Path to binary file
    Returns: 
        Any: Object Stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary File Loaded from : {path}")
    return data

