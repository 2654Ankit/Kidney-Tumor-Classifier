from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Kidney_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline 
from Kidney_Disease_Classifier.pipeline.stage_03_model_training import ModelTrainingPipeline

from Kidney_Disease_Classifier.pipeline.stage_04_model_evaluation import Evaluationpipeline

STAGE_NAME = "Data ingestion pipeline"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Prepare base model"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e





STAGE_NAME = "Training"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = Evaluationpipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

