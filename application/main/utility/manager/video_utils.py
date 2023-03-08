import os
from typing import List
from io import BytesIO
from PIL import Image
from video2images import Video2Images
from application.main.config import settings
from application.main.utility.manager.image_utils import BasicImageUtils


class BasicVideoUtils(BasicImageUtils):

    @classmethod
    async def read_video_file(cls, file, filename, cache=True) -> List[Image.Image]:
        file_input_location = os.path.join(settings.APP_CONFIG.CACHE_DIR, f"inputs/{filename}")
        file_output_location = os.path.join(settings.APP_CONFIG.CACHE_DIR, "outputs")

        # Save video to a temporary file
        with open(file_input_location, 'wb') as f:
            f.write(file)
        
        # 
        try:
            # 
            frames_location = Video2Images(video_filepath=file_input_location, out_dir=file_output_location, capture_rate=int(settings.VIDEO_CAPTURE_RATE)).out_dir
            # 
            images = []
            for filename in os.listdir(frames_location):
                if filename.endswith('.jpg'):
                    # send the file path
                    img_path = os.path.join(frames_location, filename)
                    images.append(img_path)
                    # 
                    # send the file bytes 
                    # image = cls.read_image_file(img_path, filename)
                    # images.append(image)
                    # with Image.open(BytesIO(img_path)) as img:
                    #     images.append(img)
        except:
            return []
        
        if cache:
            pass

        return images
