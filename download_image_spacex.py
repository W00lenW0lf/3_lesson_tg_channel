import requests
from saving_images import saving_images

DEFAULT_LAUNCH_NUM = 19
def download_image_spacex():
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
        image_urls = launch_array[DEFAULT_LAUNCH_NUM]["links"]["flickr"]["original"]
    raw_urls = {}
    directory = "images"
    for img_num, img_url in enumerate(image_urls, 1):
        img_name = f"spacex_image_{img_num}.jpg"
        raw_urls[img_name] = img_url
    saving_images(raw_urls, directory)

if __name__ == '__main__':
    download_image_spacex()