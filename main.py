from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DataScienceProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DataScienceProject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DataScienceProject.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


STAGE_NAME_1  = 'DATA INGESTION STAGE'
STAGE_NAME_2  = 'DATA VALIDATION STAGE'
STAGE_NAME_3 = 'DATA TRANSFORMATION STAGE'
STAGE_NAME_4 = 'Model Training Pipeline STAGE'

try:
    logger.info(f">>>>> stage {STAGE_NAME_1} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME_1} completed! <<<<<")



    logger.info(f">>>>> stage {STAGE_NAME_2} started <<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME_2} completed! <<<<<")




    logger.info(f">>>>> stage {STAGE_NAME_2} started <<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME_3} completed! <<<<<")


    logger.info(f">>>>> stage {STAGE_NAME_4} started <<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME_4} completed! <<<<<")


except Exception as e:
    logger.exception(e)
    raise e


# https://github.com/krishnaik06/Data-Science-Projects-For-Resumes