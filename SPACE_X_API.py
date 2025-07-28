import requests
from image_saver import image_saver
def SPACE_X_API():
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
        image_urls = launch_array[19]["links"]["flickr"]["original"]
    raw_urls = {}
    directory = "images/SPACE_X"
    for img_num, img_url in enumerate(image_urls, 1):
        img_name = f"spacex_image_{img_num}.jpg"
        raw_urls[img_name] = img_url
    image_saver(raw_urls, directory)