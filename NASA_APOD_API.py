import requests
import os
from urllib.parse import urlparse
from image_saver import image_saver

API_KEY = os.environ.get('API_KEY')


def NASA_APOD_API():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 10,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    launch_array = response.json()
    raw_urls = {}
    directory = "images"
    for item in launch_array:
        explanation = item["explanation"]
        name = " ".join(explanation.split()[:3]).strip(" ,.!?")
        url = item["url"]
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        _, ext = os.path.splitext(filename)
        name_with_ext = f"{name}{ext}"
        raw_urls[name_with_ext] = url
    image_saver(raw_urls, directory)
