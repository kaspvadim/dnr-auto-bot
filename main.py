import telebot
import os
import time
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Это автоматический бот доски объявлений.")

def auto_posting():
    sample_ads = [
        {"text": "🚗 Продаю ВАЗ 2107, 2005 г.в. | Донецк", "photo": None},
        {"text": "🏠 Сдаётся 1-к квартира, Центр, 15 000 руб./мес. | Макеевка", "photo": None},
        {"text": "🔧 Продам стартер на ВАЗ 2110 | Донецк", "photo": None},
    ]
    while True:
        ad = random.choice(sample_ads)
        try:
            bot.send_message(CHANNEL_ID, ad["text"])
            print("Пост опубликован:", ad["text"])
        except Exception as e:
            print("Ошибка:", e)
        time.sleep(random.randint(60, 1200))  # от 1 до 20 минут

import threading
threading.Thread(target=auto_posting).start()
bot.infinity_polling()
