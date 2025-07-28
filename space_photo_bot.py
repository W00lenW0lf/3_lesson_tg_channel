import telegram
import os
import random

def tg_bot():
    TG_TOKEN = os.environ.get('TG_TOKEN')
    bot = telegram.Bot(token=TG_TOKEN)
    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
    chat_id = updates[0].message.chat.id
    photo = random.choice([f for f in os.listdir('images')])
    with open(f'images/{photo}', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)