import requests
import random


# tg - @Codify_EmirBot

def get_last_message():
    url = "https://api.telegram.org/bot6843897717:AAFANiInEsvceqijMKdfL5nFWoG0mX6vcGU/getUpdates"
    response = requests.get(url)
    data = response.json()
    last_message = data["result"][-1]["message"]["text"]
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    return last_message, chat_id


def send_message(chat_id, text):
    url_to_send = f"https://api.telegram.org/bot6843897717:AAFANiInEsvceqijMKdfL5nFWoG0mX6vcGU/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url_to_send)


def answer_to_message():
    last_message, chat_id = get_last_message()
    if last_message == "Скажи привет":
        send_message(chat_id, "Привет")
    elif last_message == "Назови число от 1 до 10":
        send_message(chat_id, f"{random.randrange(1, 10)}")


answer_to_message()
