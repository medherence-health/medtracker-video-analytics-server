from fastapi import File, UploadFile
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance
from application.main.services.video_classification_service import VideoClassificationService
from application.main.utility.manager.video_utils import BasicVideoUtils

video_classification_service = VideoClassificationService()
router = APIRouter(prefix='/video/analyze')
logger = LoggerInstance().get_logger(__name__)
video_formats = ("mov", "avi", "mpg", "mpeg", "mp4", "mkv", "wmv")

@router.post("/")
async def video_classification(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in video_formats
    if not extension:
        return {"message": "Video must be in accepted format!", "formats": ", ".join(video_formats)}
    
    # check for video size (should not be greater than 5MB)
    content = await file.read()
    if len(content) >= 5242880:
        return {"message": "Your file is more than 5MB"}
    
    # 
    logger.info('Video Classification')
    video = await BasicVideoUtils.read_video_file(content, filename=file.filename, cache=True)
    video_category = await video_classification_service.classify(video)

    return {"message":"video analysed", "result": video_category}
