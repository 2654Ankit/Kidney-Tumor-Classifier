from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data ingestion pipeline"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e



            