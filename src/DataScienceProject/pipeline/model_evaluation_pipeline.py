from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.model_evaluationn import ModelEvaluation
from src.DataScienceProject import logger

STAGE_NAME = 'Model Evaluation Stage'

class ModelEvalationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):

        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = ModelEvalationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\nx=========x')
    except Exception as e:
        logger.exception(e)
        raise e