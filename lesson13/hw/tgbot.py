import time
import requests
from tg_class import TelegramBot


answered = []

products = [
    {"name": "Кружка", "price": 159, "photo": "cup.jpg"}, 
    {"name": "Зонт", "price": 700, "photo": "cup.jpg"},
    {"name": "Сумка", "price": 2500, "photo": "cup.jpg"},
]

# products = [product_1, product_2, product_3]


def say_hello(chat_id, bot):  # bot = 'python'
    txt_to_say = "hello world"
    bot.send_message(chat_id=chat_id, txt=txt_to_say)


def send_weather(chat_id, txt, telegram_bot):
    txt_lst = txt.split()
    city = txt_lst[-1]
    weather_api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    response = requests.get(weather_api)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = round(weather_data['main']['temp'])
        txt_to_say = f"{temperature} °C"
    else:
        txt_to_say = "No such city, check it"
    telegram_bot.send_message(chat_id=chat_id, txt=txt_to_say)


def send_product(chat_id, num, telegram_bot):
    name = products[num]["name"]
    price = products[num]["price"]
    photo = open(products[num]["photo"], 'rb')
    telegram_bot.send_message(chat_id, name)
    telegram_bot.send_message(chat_id, f"{price} сом")
    telegram_bot.send_photo(chat_id, photo)


telegram_bot = TelegramBot()
while True:
    chat_id, txt, message_id = telegram_bot.get_last_message()
    if message_id not in answered:
        print(chat_id)
        if txt == "say hello":
            say_hello(chat_id, telegram_bot)
        elif txt.startswith("weather"):  # текст начинается с weather
            send_weather(chat_id, txt, telegram_bot)
        elif txt == "cat":
            fl = open("cat.jpg", 'rb')
            telegram_bot.send_photo(chat_id, fl)
        elif txt in ["1", "2", "3"]:
            product_num = int(txt) - 1
            send_product(chat_id, product_num, telegram_bot)
            
    answered.append(message_id)
    time.sleep(1)
