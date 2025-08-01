import telegram
import os
import random
import time
from threading import Thread
from dotenv import load_dotenv


def get_all_images():
    images = []
    for root, _, files in os.walk('images'):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                images.append(os.path.join(root, file))
    return images


def send_and_delete_photos(bot, chat_id, img_sending_delay):
    while True:
        try:
            images = get_all_images()
            if not images:
                print("Нет доступных изображений.")
                time.sleep(img_sending_delay)
                continue
            photo = random.choice(images)
            with open(photo, 'rb') as photo_file:
                bot.send_photo(chat_id=chat_id, photo=photo_file)
            os.remove(photo)
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(img_sending_delay)


def send_images_bot(tg_token, img_sending_delay):
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    chat_id = updates[0].message.chat.id
    send_and_delete_photos(bot, chat_id, img_sending_delay)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ.get('TG_TOKEN')
    img_sending_delay = int(os.environ.get('IMG_SENDING_DELAY'))
    send_images_bot(tg_token, img_sending_delay)
