import os
import urllib.request as request
from src.DataScienceProject import logger
import zipfile
from src.DataScienceProject.entity.config_entity import DataIngestionConfig


# component-data Ingestion
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    # Dwnloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
          filename,headers = request.urlretrieve(
              url= self.config.source_url,
              filename=self.config.local_data_file
          )
          logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f"File Already exists")  
    
    def extract_zip_file(self):
        """Zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'Zip file extracted to {unzip_path}')

