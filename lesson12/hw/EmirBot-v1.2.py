import random
import time
import requests
from product_model import products_list

# @Codify_EmirBot

TOKEN = "6843897717:AAFANiInEsvceqijMKdfL5nFWoG0mX6vcGU"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

answered = []


def get_last_message():
    url = BASE_URL + "/getUpdates"
    response = requests.get(url)
    data = response.json()
    txt = data["result"][-1]["message"]["text"]
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_id = data["result"][-1]["message"]["message_id"]
    return chat_id, txt, message_id


def send_message(chat_id, txt_to_say):
    url_to_send = f"{BASE_URL}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": txt_to_say
    }
    requests.get(url_to_send, params=params)


def send_photo(chat_id, fl):
    url_to_send = f"{BASE_URL}/sendPhoto"
    params = {
        "chat_id": chat_id,
    }
    files = {"photo": fl}
    requests.get(url_to_send, params=params, files=files)


def send_gif(chat_id, animation):
    url_to_send = f"{BASE_URL}/sendAnimation"
    params = {
        "chat_id": chat_id,
        "animation": animation
    }
    requests.get(url_to_send, params=params)


def send_sticker(chat_id, sticker):
    url_to_send = f"{BASE_URL}/sendSticker"
    params = {
        "chat_id": chat_id,
        "sticker": sticker
    }
    requests.get(url_to_send, params=params)


def say_hello(chat_id):
    txt_to_say = "Привет"
    send_message(chat_id, txt_to_say)


def say_random_num(chat_id):
    txt_to_say = f"{random.randrange(1, 10)}"
    send_message(chat_id, txt_to_say)


def send_products(chat_id, product_id):
    name = products_list[product_id].name
    price = products_list[product_id].price
    photo = products_list[product_id].photo
    send_message(chat_id, txt_to_say=name)
    send_message(chat_id, txt_to_say=f"{price} сом")
    send_photo(chat_id, fl=open(photo, "rb"))


while True:
    chat_id, txt, message_id = get_last_message()

    if message_id not in answered:
        print(chat_id)
        if txt == "привет":
            say_hello(chat_id)
        elif txt == "назови число от 1 до 10":
            say_random_num(chat_id)
        elif txt == "фото":
            fl = open("cat.jpg", 'rb')
            send_photo(chat_id, fl)
        elif txt == "гифка":
            # animation = "CgACAgIAAxkBAAICOGZxPlmHZxCFYcuUNtqJ7Xt8aOhtAAIWSgACyguIS6IgZMLlfmy3NQQ"
            animation = "https://i.pinimg.com/originals/22/30/e9/2230e960b76375b0224494ffe27e1d44.gif"
            send_gif(chat_id, animation)
        elif txt == "стикер":
            sticker_list = [
                "CAACAgIAAxkBAAEMVVRmcTxB4CR7y6qTprbB0jDImUzVvQACqSEAAsNGaEsRQ1Q-0S5RGDUE",
                "CAACAgIAAxkBAAEMVUxmcTjWd2Dli-spy29tids1se4sugACjjgAAnI2kEicZQTyPOEh3jUE",
                "CAACAgIAAxkBAAEMVVVmcTxSX2UHEuGtmUcZIoKtWwEhPwACNhUAAgeD6UhtOpxP5V5mEDUE",
                "CAACAgIAAxkBAAEMVVBmcTpRofxkmc_2azzheW9xx9WWEAACwFMAAjg9KUlKNWOGv4IRzzUE",
                "CAACAgIAAxkBAAEMVVZmcTxdjjwemOTKG_NgR3VMOOszkQACyx8AAmcOaUtu9AkpEX33FDUE"
            ]
            sticker = random.choice(sticker_list)
            send_sticker(chat_id, sticker)
        elif txt in ["1", "2", "3"]:
            product_id = int(txt) - 1
            send_products(chat_id, product_id)

    answered.append(message_id)
    time.sleep(1)
