import re
import requests
from typing import Dict, List, Optional, Union
from decouple import config
from bs4 import BeautifulSoup
from .save import save_images, save_video


class VideoIsInvalid(Exception):
    pass


class TikTok:
    def __init__(self, url: str) -> None:
        self.url = url
        
        self.headers = {
            "Host": "musicaldown.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "TE": "trailers",
        }
        
        self.server_url = "https://musicaldown.com/"
        self.post_url = self.server_url + "id/download"
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.request = self.session.get(self.server_url)
        
    def extract_link(self) -> Dict[str, str]:
        data = {}
        
        parse = BeautifulSoup(self.request.text, "html.parser")
        get_input = parse.findAll("input")
        
        for index in get_input:
            if index.get("id") == "link_url":
                data[index.get("name")] = self.url
            else:
                data[index.get("name")] = index.get("value")
        return data
        
    def check_request_status(self, request: requests) -> Optional[Exception]:
        if request.status_code == 302 \
        or "This video is currently not available" in request.text \
        or "Video is private or removed!" in request.text \
        or "Submitted Url is Invalid, Try Again" in request.text:
            raise VideoIsInvalid("Video is invalid!")
        
    def get_video_blank(self, request: requests) -> requests.Response:
        video_blank = BeautifulSoup(request.text, "html.parser").findAll(
            "a", attrs={"target": "_blank"})[0].get("href")
        return video_blank

    def get_photo_blanks(self, request: requests) -> List[requests.Response]:
        image_blank_group = []
        image_blanks = BeautifulSoup(request.text, "html.parser").findAll(
            "img", attrs={"loading": "lazy"})

        for image_blank in image_blanks:
            download_link = image_blank.get("src")
            image_blank_group.append(download_link)
        return image_blank_group
        
    def download_tiktok(self, selected_value: str) -> Dict[str, str]:
        data = self.extract_link()
        request_post = self.session.post(self.post_url, data=data, allow_redirects=True)
        
        self.check_request_status(request_post)
        
        match selected_value:
            case "video":
                """ Receiving request tuple """
                request_blank = self.get_video_blank(request_post)
                return save_video(request_blank)
                
            case "photo":
                """ Receiving requests list """
                request_blank = self.get_photo_blanks(request_post)
                return save_images(request_blank)