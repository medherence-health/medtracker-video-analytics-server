from typing import List, Dict
from collections import defaultdict
from pathlib import Path
from imageai.Prediction.Custom import CustomImagePrediction
# 
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
from application.initializer import LoggerInstance
# from PIL import Image
import numpy as np
# import tensorflow as tf
import ssl
# 

ssl._create_default_https_context = ssl._create_unverified_context
logger = LoggerInstance().get_logger(__name__)
classifier_model = None


def merge_dicts(dicts_list):
    """
        To merge a list of dictionaries while taking the mean of values for repeated keys
    """
    merged_dict = defaultdict(lambda: {'sum': 0, 'count': 0})
    for d in dicts_list:
        for k, v in d.items():
            merged_dict[k]['sum'] += v
            merged_dict[k]['count'] += 1
    mean_dict = {k: v['sum'] / v['count'] for k, v in merged_dict.items()}
    return mean_dict


class InferenceTask:
    """
        Split video into frames, classify each frame, and ensemble the results
    """
    @staticmethod
    async def load_model(classifier_model_name):
        if len(classifier_model_name) != 0:
            model = CustomImagePrediction()
            model.setModelPath(model_path=classifier_model_name['model']) # "action_net_ex-060_acc-0.745313.h5"
            model.setJsonPath(model_json=classifier_model_name['classes']) # "model_class.json" https://raw.githubusercontent.com/OlafenwaMoses/Action-Net/master/model_class.json
            model.loadFullModel(num_objects=16)

        return model
    
    @staticmethod
    async def decode_results(results: List[zip]) -> List[Dict[str, float]]:
        # Dict[str, float]
        decoded_results = []
        # decoded_results = {}
        for result in results:
            _results = []
            for prediction, probability in result:
                resp = {}
                resp[prediction] = probability
                # resp["confidence"] = probability # f"{round(probability, 2):0.2f} %"
                _results.append(resp) 
            # 
            # print(_results)
            _merged_results = merge_dicts(_results)
            decoded_results.append(_merged_results)

        merged_results = merge_dicts(decoded_results)
        return merged_results
    
    async def predict(self, classifier_model_name, video: List[Path]) -> List:
        if len(video) is 0:
            return {"message": "Server failed to process file"}
        # 
        global classifier_model
        if classifier_model is None:
            classifier_model = await self.load_model(classifier_model_name)
        # 
        results = []
        # 
        for image in video:
            predictions, probabilities = classifier_model.classifyImage(image_input=image, result_count=5)
            results.append(zip(predictions, probabilities))

        response = await self.decode_results(results) # f"{round(probability, 2):0.2f} %"
        return response
# 
# 
# https://github.com/AbhishekSalian/Video2Images
# https://github.com/bhimrazy/Image-Recognition-App-using-FastAPI-and-PyTorch
# 
# 
# def run_predict(image_file_path: str = "images/5.jpg"):
#     predictor = CustomImagePrediction()
#     predictor.setModelPath(model_path="action_net_ex-060_acc-0.745313.h5")
#     predictor.setJsonPath(model_json="model_class.json")
#     predictor.loadFullModel(num_objects=16)


#     # predictions, probabilities = predictor.predictImage(image_input=image_file_path, result_count=4)
#     predictions, probabilities = predictor.classifyImage(image_input=image_file_path, result_count=4)
#     # for prediction, probability in zip(predictions, probabilities):
#     #     print(prediction, " : ", probability)

#     return predictions, probabilities
# 
# https://stackoverflow.com/questions/36758945/how-to-merge-a-list-of-dicts-summing-values-for-repeated-keys



