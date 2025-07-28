import telegram
import os

def tg_bot():
    TG_TOKEN = os.environ.get('TG_TOKEN')
    bot = telegram.Bot(token=TG_TOKEN)
    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
    chat_id = updates[0].message.chat.id
    bot.send_message(chat_id=chat_id, text="Some text")