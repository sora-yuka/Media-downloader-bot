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
        file.write(response.content)
    return path

def save_images(request_blank_list: List[requests.Response]) -> List[os.path]:
    path = os.path.join(f"{os.getcwd()}/source/photo")
    path_to_photos = []
    
    for request_blank in request_blank_list:
        response = requests.get(request_blank)
        random_name = randint(000000, 999999)
        
        with open(f"source/photo/{random_name}.jpg", "wb") as file:
            file.write(response.content)
    
        path_to_photos.append(path + f"/{random_name}.jpg")
    return path_to_photos