from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.components.prepare_base_model import PrepareBaseaModel
from Kidney_Disease_Classifier.config.configuration import ConfigurationManager


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
    
            prepare_base_model = PrepareBaseaModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise e

if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    