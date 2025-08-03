import requests
import os
from urllib.parse import urlparse
from saving_images import saving_images
from dotenv import load_dotenv


def download_image_nasa_apod(number_images_saved):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": number_images_saved,
        "api_key": NASA_API_KEY
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
    saving_images(raw_urls, directory)


if __name__ == '__main__':
    load_dotenv()
    NASA_API_KEY = os.environ.get('NASA_API_KEY')
    number_images_saved = os.environ.get('NUMBER_IMAGES_SAVED')
    download_image_nasa_apod(number_images_saved)
