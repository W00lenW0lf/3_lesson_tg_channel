import telegram
import os
import random
import time
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
        except telegram.error.TelegramError as error:
            print(f"Ошибка: {error}")
        time.sleep(img_sending_delay)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ.get('TG_TOKEN')
    img_sending_delay = int(os.environ.get('IMG_SENDING_DELAY'))
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    chat_id = updates[1].message.chat.id
    send_and_delete_photos(bot, chat_id, img_sending_delay)