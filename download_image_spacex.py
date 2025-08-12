import requests
import os
from save_images import save_images
from dotenv import load_dotenv


def download_image_spacex(default_launch_num):
    url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)
    response.raise_for_status()
    launch_array = response.json()
    image_urls = launch_array["links"]["flickr"]["original"]
    if not image_urls:
        url = "https://api.spacexdata.com/v5/launches/"
        response = requests.get(url)
        response.raise_for_status()
        launch_array = response.json()
        image_urls = launch_array[int(default_launch_num)]["links"]["flickr"]["original"]
    raw_urls = {}

    for img_num, img_url in enumerate(image_urls, 1):
        img_name = f"spacex_image_{img_num}.jpg"
        raw_urls[img_name] = img_url
    save_images(raw_urls, params=None)


if __name__ == '__main__':
    load_dotenv()
    default_launch_num = os.environ.get('DEFAULT_LAUNCH_NUM')
    download_image_spacex(default_launch_num)