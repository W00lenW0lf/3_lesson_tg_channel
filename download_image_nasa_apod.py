import requests
import os
from urllib.parse import urlparse
from save_images import save_images
from dotenv import load_dotenv


def download_image_nasa_apod(saved_images_count, nasa_api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": saved_images_count,
        "api_key": nasa_api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    array_of_launches = response.json()
    raw_urls = {}
    for launch in array_of_launches:
        explanation = launch["explanation"]
        name = " ".join(explanation.split()[:3]).strip(" ,.!?")
        url = launch["url"]
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        _, ext = os.path.splitext(filename)
        name_with_ext = f"{name}{ext}"
        raw_urls[name_with_ext] = url
    save_images(raw_urls, params=None)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    saved_images_count = os.environ.get('SAVED_IMAGES_COUNT')
    download_image_nasa_apod(saved_images_count, nasa_api_key)

