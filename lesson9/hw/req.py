import requests
import random

# 1) Say Hello

url = ("https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/getUpdates")
response = requests.get(url)
data = response.json()  # json == dictionary
txt = data["result"][-1]["message"]["text"]
print(txt)


def bot_greeting():
    if txt == "say hello":
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        return chat_id


def result():
    chat_id = bot_greeting()
    txt_to_say = "Hello World"
    url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={txt_to_say}"
    requests.get(url_to_send)


result()


# 2) Анекдоты

def if_joke():
    if txt == "анекдот":
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        return chat_id


def gif_u_joke():
    chat_id = if_joke()
    txt_to_say = random.randint(0, 10)
    if txt_to_say < 3:
        joke = """Врач говорит больному: Вам нельзя пить, курить, увлекаться случайным сексом, играть в карты…
        Больной: Доктор, скажите честно: тут уже была моя Софочка?"""
        url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
        return url_to_send
    elif txt_to_say > 3 and txt_to_say < 6:
        joke = """Штирлицу за шиворот упала гусеница. "Где-то взорвался танк," -- подумал Штирлиц."""
        url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
        return url_to_send
    else:
        joke = "Одна девочка так сильно боялась прыгать с парашютом, что прыгнула без него"
        url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
        return url_to_send


def joke_print():
    url_to_send = gif_u_joke()
    print(f"Connection: {requests.get(url_to_send)}")


joke_print()










# def print_joke():
#     if txt == "анекдот":
#         chat_id = data["result"][-1]["message"]["chat"]["id"]
#         txt_to_say = random.randint(0, 10)
#         if txt_to_say < 3:
#             joke = """Врач говорит больному: Вам нельзя пить, курить, увлекаться случайным сексом, играть в карты…
#             Больной: Доктор, скажите честно: тут уже была моя Софочка?"""
#             url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
#             requests.get(url_to_send)
#             print(joke)
#         elif txt_to_say > 3 and txt_to_say < 6:
#             joke = """Штирлицу за шиворот упала гусеница. "Где-то взорвался танк," -- подумал Штирлиц."""
#             url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
#             requests.get(url_to_send)
#             print(joke)
#         else:
#             joke = "Одна девочка так сильно боялась прыгать с парашютом, что прыгнула без него"
#             url_to_send = f"https://api.telegram.org/bot7283576861:AAG6wNwx0S1LwxMrxUK3Ph61-tuKxLU8zs4/sendMessage?chat_id={chat_id}&text={joke}"
#             requests.get(url_to_send)
#             print(joke)
#
#
# print_joke()


