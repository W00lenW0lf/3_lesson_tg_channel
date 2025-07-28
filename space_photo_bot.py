import telegram
import os
import random
import time
from threading import Thread


def get_all_images():
    images = []
    for root, _, files in os.walk('images'):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                images.append(os.path.join(root, file))
    return images


def send_and_delete_photos(bot, chat_id,DELAY):
    while True:
        try:
            images = get_all_images()
            if not images:
                print("Все фото отправлены и удалены!")
                time.sleep(DELAY)
                continue
            photo = random.choice(images)
            with open(photo, 'rb') as f:
                bot.send_photo(chat_id=chat_id, photo=f)
                print(f"Отправлено и будет удалено: {photo}")
            os.remove(photo)
            time.sleep(DELAY)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(60)


def tg_bot():
    TG_TOKEN = os.environ.get('TG_TOKEN')
    DELAY = os.environ.get('DELAY')
    bot = telegram.Bot(token=TG_TOKEN)
    updates = bot.get_updates()
    chat_id = updates[0].message.chat.id
    Thread(target=send_and_delete_photos, args=(bot, chat_id,DELAY)).start()
