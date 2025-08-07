import requests
import os
from urllib.parse import urlparse
from save_images import save_images
from dotenv import load_dotenv


def download_image_nasa_apod(number_saved_images, nasa_api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": number_saved_images,
        "api_key": nasa_api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    array_of_launches = response.json()
    raw_urls = {}
    directory = "images"
    for launch in array_of_launches:
        explanation = launch["explanation"]
        name = " ".join(explanation.split()[:3]).strip(" ,.!?")
        url = launch["url"]
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        _, ext = os.path.splitext(filename)
        name_with_ext = f"{name}{ext}"
        raw_urls[name_with_ext] = url
    save_images(raw_urls, directory)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    number_saved_images = os.environ.get('NUMBER_SAVED_IMAGES')
    download_image_nasa_apod(number_saved_images, nasa_api_key)

