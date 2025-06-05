import os
import pandas as pd
from src.DataScienceProject import logger
import zipfile
from src.DataScienceProject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = False
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    logger.info(f'Column {col} is not in the schema.')
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation Status is : {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation Status is : {validation_status}')
            return validation_status

        except Exception as e:
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f'Validation Status is : {e}')
            logger.error(f'An error occurred while validating the data: {e}')
            raise e

    def validate_column_types(self) -> bool:
        """
        Validate that each column has the expected data type according to the schema.
        """
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            schema = self.config.all_schema
            status = True

            for column, expected_type in schema.items():
                if column in data.columns:
                    actual_dtype = str(data[column].dtype)
                    # Simplified dtype comparison
                    if expected_type == "int" and not pd.api.types.is_integer_dtype(data[column]):
                        logger.warning(f"Column '{column}' is expected to be int but found {actual_dtype}")
                        status = False
                    elif expected_type == "float" and not pd.api.types.is_float_dtype(data[column]):
                        logger.warning(f"Column '{column}' is expected to be float but found {actual_dtype}")
                        status = False
                    elif expected_type == "object" and not pd.api.types.is_object_dtype(data[column]):
                        logger.warning(f"Column '{column}' is expected to be object/string but found {actual_dtype}")
                        status = False
                else:
                    logger.warning(f"Column '{column}' not found in dataset")
                    status = False

            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f'\nColumn Type Validation Status: {status}')

            return status

        except Exception as e:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f'\nColumn Type Validation Error: {e}')
            logger.error(f'Error during column type validation: {e}')
            raise e


