from src.DataScienceProject import logger
import pandas as pd 
from sklearn.linear_model import ElasticNet
import joblib # Alternative of pickle
from src.DataScienceProject.entity.config_entity import ModelTrainingConfig
import os


class ModelTrainer:
    def __init__(self,config: ModelTrainingConfig):
        self.config = config
        # self.model = ElasticNet(alpha=config.alpha, l1_ratio=config.l1_ratio)
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop(columns=[self.config.target_column],axis=1)
        test_x = test_data.drop(columns=[self.config.target_column],axis=1)

        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        lr.fit(train_x, train_y)
        print("Train Path Exists:", os.path.exists(self.config.train_data_path))
        print("Test Path Exists:", os.path.exists(self.config.test_data_path))

        logger.info('Model fit training done.')


        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))