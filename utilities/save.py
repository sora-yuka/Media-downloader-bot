import os
import requests
from typing import List


path = os.path.join(os.getcwd(), "source/photo", "../video")
os.makedirs(path, exist_ok=True)

def save_video(media_content: requests.Response) -> os.path:
    path = os.path.join(f"{os.getcwd()}/source/video/", "VideoFile.mp4")
    
    with open("source/video/VideoFile.mp4", "wb") as file:
        file.write(media_content.content)
    return path

def save_images(media_contents: List[requests.Response]) -> os.path:
    path = os.path.join(f"{os.getcwd()}/source/photo")
        
    for media_content in media_contents:
        random_name = randint(000000, 999999)
        with open(f"source/photo/{random_name}.jpg", "wb") as file:
            file.write(media_content.content)
    return path