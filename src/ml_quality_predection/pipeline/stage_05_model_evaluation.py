from ml_quality_predection.config.configuration import ConfigurationManager
from ml_quality_predection.components.model_evaluation import ModelEvaluation
from ml_quality_predection import logger


STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()
