import requests
import os
from saving_images import saving_images
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()
NASA_API_KEY = os.environ.get('NASA_API_KEY')


def download_image_nasa_epic():
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    params = {
        "api_key": NASA_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    array_of_launches = response.json()
    raw_urls = {}
    directory = "images"
    for photo in array_of_launches:
        photo_date = photo["date"]
        photo_date = datetime.strptime(photo_date, "%Y-%m-%d %H:%M:%S")
        photo_name = photo["image"] + ".png"
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        photo_path = f"{photo_date:%Y/%m/%d}/png/{photo_name}"
        params = {'api_key': NASA_API_KEY}
        epic_url = f"{base_url}/{photo_path}?{urlencode(params)}"
        print(epic_url)
        raw_urls[photo_name] = epic_url
    saving_images(raw_urls, directory)


if __name__ == '__main__':
    download_image_nasa_epic()
