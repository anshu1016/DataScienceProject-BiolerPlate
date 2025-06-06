import os
from src.DataScienceProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd 
from src.DataScienceProject.entity.config_entity import DataTransformationConfig
class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    
    ## You can add different data transformation technoqies such as Scaler, PCA and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_splitting bcz data is already cleaned up.
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        # SPlit the data into training and test dataset
        train,test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Splitted data into training and test sets')
        logger.info(f'The Train Data SHAPE is: {train.shape}')
        logger.info(f'The Test Data SHAPE is: {test.shape}')

        print(train.shape)
        print(test.shape)

        