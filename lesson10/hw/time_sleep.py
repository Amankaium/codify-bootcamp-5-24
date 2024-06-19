import time
import requests
import random

TOKEN = "6951830702:AAGdXJDi416NAV0Zy4k0cLaaw3LB8pMe_tI"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
answered = []

def get_last_message():
    url = BASE_URL + "/getUpdates"
    response = requests.get(url)
    data = response.json()
    if "result" in data and data["result"]:
        print(data["result"][-1])
        last_message = data["result"][-1]["message"]
        txt = last_message.get("text", "")
        chat_id = last_message["chat"]["id"]
        message_id = last_message["message_id"]
        return chat_id, txt, message_id
    else:
        return None, None, None


def send_message(chat_id, text):
    url_to_send = f'{BASE_URL}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text':text
    }
    requests.get(url_to_send, params=params)


def send_photo(chat_id, photo_path):
    url_to_send = f'{BASE_URL}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id}
    requests.get(url_to_send, params= params, files= files)


def send_stick(chat_id):
    sticks = ['CAACAgQAAxkBAAICD2ZyXwHZYPspY9TknMRLxGpliUsCAAL9AANrrl4JFyHAPwhZO041BA']
    sticker_id = random.choice(sticks)
    url_to_send = f'{BASE_URL}/sendSticker'
    params = {'chat_id': chat_id, 'sticker': sticker_id}
    requests.get(url_to_send, params=params)

def say_hello(chat_id):
    send_message(chat_id, "hello world")


def send_weather(chat_id, txt):
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
    send_message(chat_id, txt_to_say)


while True:
    chat_id, txt, message_id = get_last_message()

    if message_id not in answered:
        print(chat_id)
        if txt == "say hello":
            say_hello(chat_id)
        elif txt.startswith("weather"):  # текст начинается с weather
            send_weather(chat_id, txt)
        elif txt == "cat":
            send_photo(chat_id, 'cat.jpg')
        elif txt == 'sticker':
            send_stick(chat_id)

    answered.append(message_id)
    time.sleep(1)
