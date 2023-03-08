from application.main.config import settings
from application.initializer import LoggerInstance
from application.main.infrastructure.classification.video.inference import InferenceTask


class VideoClassificationService(object):

    def __init__(self):
        self.logger = LoggerInstance().get_logger(__name__)
        self.video_model = InferenceTask()
        self.image_classification_model = settings.APP_CONFIG.ACTION_NET_IMAGE_CLASSIFICATION_MODEL
        self.image_classification_model_classes = settings.APP_CONFIG.ACTION_NET_IMAGE_CLASSIFICATION_MODEL_CLASSES

    async def classify(self, video_data):
        self.logger.info(f'Model IN use : {self.image_classification_model}')
        label = await self.video_model.predict(classifier_model_name={"model": self.image_classification_model, "classes": self.image_classification_model_classes}, video=video_data)
        return label
