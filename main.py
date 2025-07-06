import telebot
import time
import random
from config import BOT_TOKEN, CHANNEL_ID

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Чтобы подать объявление, нажмите кнопку в меню.")

def publish_auto_post():
    sample_ads = [
        {"text": "🚗 Продается ВАЗ 2109, 2005 г.в. Цена: 150 000 руб. Тел: +7-999-000-00-00", "photo": "https://picsum.photos/400"},
        {"text": "🏠 Сдам 1-комн. квартиру в Донецке. 8 000 руб/мес. Тел: +7-999-111-11-11", "photo": "https://picsum.photos/401"}
    ]
    post = random.choice(sample_ads)
    try:
        bot.send_photo(CHANNEL_ID, post["photo"], caption=post["text"])
    except Exception as e:
        print("Ошибка при публикации:", e)

print("Бот запущен.")

while True:
    publish_auto_post()
    time.sleep(random.randint(60, 1200))
