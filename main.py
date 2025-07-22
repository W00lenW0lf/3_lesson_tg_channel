import requests
import os
from urllib.parse import urlparse

API_KEY = os.environ.get('API_KEY')


def fetch_spacex_last_launch(launch_num):
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    response.raise_for_status()
    launch_json = response.json()
    one_launch = launch_json[launch_num]
    image_urls = one_launch["links"]["flickr"]["original"]
    raw_urls = {}
    for img_num, img_url in enumerate(image_urls, 1):
        img_name = f"spacex_image_{img_num}.jpg"
        raw_urls[img_name] = img_url
    return (raw_urls)  # name:link


def astronomy_picture_of_the_day():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 10,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    launch_array = response.json()
    raw_urls = {}
    for item in launch_array:
        explanation = item["explanation"]
        name = " ".join(explanation.split()[:3]).strip(" ,.!?")
        url = item["url"]
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        _, ext = os.path.splitext(filename)
        name_with_ext = f"{name}{ext}"
        raw_urls[name_with_ext] = url
    return (raw_urls)  # name:link


def earth_polychromatic_imaging_camera():
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    params = {
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    launch_array = response.json()
    raw_urls = {}
    for photo in launch_array:
        photo_date = photo["date"]
        date_part, time_part = photo_date.split()
        year, month, day = date_part.split('-')
        photo_name = photo["image"] + ".png"
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{photo_name}?api_key={API_KEY}"
        raw_urls[photo_name] = epic_url
    return (raw_urls)  # name:link


def image_saver(raw_urls):
    os.makedirs('images', exist_ok=True)
    for filename, url in raw_urls.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_path = os.path.join('images', filename)
            with open(img_path, 'wb') as f:
                f.write(response.content)
            print(f"Успешно сохранено: {img_path}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке {filename}: {e}")
        except IOError as e:
            print(f"Ошибка при сохранении {filename}: {e}")


if __name__ == '__main__':
    launch_num = 19
    raw_urls = {}
    raw_urls.update(fetch_spacex_last_launch(launch_num))
    raw_urls.update(astronomy_picture_of_the_day())
    raw_urls.update(earth_polychromatic_imaging_camera())
    image_saver(raw_urls)
