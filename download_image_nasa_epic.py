import requests
import os
from save_images import save_images
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
    for photo in array_of_launches:
        photo_date = photo["date"]
        photo_date = datetime.strptime(photo_date, "%Y-%m-%d %H:%M:%S")
        photo_name = f"{photo['image']}.png"
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        photo_path = f"{photo_date:%Y/%m/%d}/png/{photo_name}"
        epic_url = f"{base_url}/{photo_path}"
        raw_urls[photo_name] = epic_url
    save_images(raw_urls, params)



if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    download_image_nasa_epic(nasa_api_key)
