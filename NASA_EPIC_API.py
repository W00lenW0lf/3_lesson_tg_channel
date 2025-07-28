import requests
import os
from image_saver import image_saver

API_KEY = os.environ.get('API_KEY')


def NASA_EPIC_API():
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    params = {
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    launch_array = response.json()
    raw_urls = {}
    directory = "images"
    for photo in launch_array:
        photo_date = photo["date"]
        date_part, time_part = photo_date.split()
        year, month, day = date_part.split('-')
        photo_name = photo["image"] + ".png"
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{photo_name}?api_key={API_KEY}"
        raw_urls[photo_name] = epic_url
    image_saver(raw_urls, directory)
