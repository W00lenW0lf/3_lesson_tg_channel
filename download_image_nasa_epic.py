import requests
import os
from saving_images import saving_images
from datetime import datetime
from dotenv import load_dotenv


def download_image_nasa_epic(nasa_api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    params = {
        "api_key": nasa_api_key
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
        params = {'api_key': nasa_api_key}
        epic_url = f"{base_url}/{photo_path}{params}"
        raw_urls[photo_name] = epic_url
    saving_images(raw_urls, directory)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    download_image_nasa_epic(nasa_api_key)
