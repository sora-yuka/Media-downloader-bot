import os
import requests
from random import randint
from typing import List

path = os.path.join(os.getcwd(), "source/photo", "../video")
os.makedirs(path, exist_ok=True)

def save_video(request_blank: requests.Response) -> os.path:
    path = os.path.join(f"{os.getcwd()}/source/video/", "VideoFile.mp4")
    response = requests.get(request_blank)
    
    with open("source/video/VideoFile.mp4", "wb") as file:
        file.write(media_content.content)
    return path

def save_images(request_blank_list: List[requests.Response]) -> os.path:
    path = os.path.join(f"{os.getcwd()}/source/photo")
    response = []
    
    for request_blank in request_blank_list:
        random_name = randint(000000, 999999)
        
        with open(f"source/photo/{random_name}.jpg", "wb") as file:
            file.write(request_blank.content)
    
        response.append(path + f"/{random_name}.jpg")
    return response