import os
import requests


def image_saver(raw_urls, directory):
    os.makedirs(directory, exist_ok=True)
    for filename, url in raw_urls.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_path = os.path.join(directory, filename)
            with open(img_path, 'wb') as f:
                f.write(response.content)
            print(f"Успешно сохранено: {img_path}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке {filename}: {e}")
        except IOError as e:
            print(f"Ошибка при сохранении {filename}: {e}")
