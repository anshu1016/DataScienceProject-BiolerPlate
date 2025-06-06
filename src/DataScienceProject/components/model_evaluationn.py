import pandas as pd  
import numpy as np  
import os
import mlflow
import mlflow.sklearn
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from urllib.parse import urlparse
from src.DataScienceProject.utils.shared import save_json
from pathlib import Path
from src.DataScienceProject.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mflow_uri)
        tracking_url_type_store = urlparse(self.config.mflow_uri).scheme


        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rmse,mae,r2) = self.eval_metrics(test_y, predicted_qualities)

            # sAVING mETRICS AS lOCAL
            scores = {'rmse':rmse,'mae':mae, 'r2':r2}

            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('rmse ',rmse)
            mlflow.log_metric('mae ',mae)
            mlflow.log_metric('r2 ',r2)
            

            # Model Registry does not work with file store
            if tracking_url_type_store != 'file':
                mlflow.sklearn.log_model(model,artifact_path="model",registered_model_name='Elasticnet Model')
            else:
                mlflow.sklearn.log_model(model,'model')

