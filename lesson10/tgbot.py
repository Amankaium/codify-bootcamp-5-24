import time
import requests


TOKEN = "7462059310:AAGeGQTueeN5B-aLx1FjqwiIOBoupJ5yg7k"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

answered = []


def get_last_message():
    url = BASE_URL + "/getUpdates"
    response = requests.get(url)
    data = response.json()  # json == dictionary
    txt = data["result"][-1]["message"]["text"]
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_id = data["result"][-1]["message"]["message_id"]
    return chat_id, txt, message_id


def send_message(chat_id, txt):
    url_to_send = f"{BASE_URL}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": txt
    }
    requests.get(url_to_send, params=params)


def say_hello(chat_id):
    txt_to_say = "hello world"
    url_to_send = f"{BASE_URL}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": txt_to_say
    }
    requests.get(url_to_send, params=params)


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
    url_to_send = f"{BASE_URL}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": txt_to_say
    }
    requests.get(url_to_send, params=params)


while True:
    chat_id, txt, message_id = get_last_message()
    if message_id not in answered:
        print(chat_id)
        if txt == "say hello":
            say_hello(chat_id)
        elif txt.startswith("weather"):  # текст начинается с weather
            send_weather(chat_id, txt)
        elif txt == "cat":
            fl = open("cat.jpg", 'rb')
            url_to_send = f"{BASE_URL}/sendPhoto"
            params = {
                "chat_id": chat_id,
            }
            files = {"photo": fl}
            requests.get(url_to_send, params=params, files=files)

    answered.append(message_id)
    time.sleep(1)
