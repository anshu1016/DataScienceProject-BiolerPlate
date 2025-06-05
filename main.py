from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
STAGE_NAME = 'DATA INGESTION STAGE'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


# https://github.com/krishnaik06/Data-Science-Projects-For-Resumes