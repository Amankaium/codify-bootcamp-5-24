import requests
from random import random

url = "https://api.telegram.org/bot7074152795:AAFiS_4--4zHy6iWDv3VKbbzvCxB7iSPZ34/getUpdates"
response = requests.get(url)
data = response.json()
txt = data["result"][-1]["message"]["text"]
print(txt)

if txt == "привет":
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    txt_to_say = "Здравствуйте!"
    url_to_send = f"https://api.telegram.org/bot7074152795:AAFiS_4--4zHy6iWDv3VKbbzvCxB7iSPZ34/sendMessage?chat_id={chat_id}&text={txt_to_say}"
    requests.get(url_to_send)

elif txt == "анекдот":
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    txt_to_say = ("Жена мужу: \n Где зарплата? \n Украли… \n У какой еще крали?")
    url_to_send = f"https://api.telegram.org/bot7074152795:AAFiS_4--4zHy6iWDv3VKbbzvCxB7iSPZ34/sendMessage?chat_id={chat_id}&text={txt_to_say}"
    requests.get(url_to_send)

elif txt == "погода":
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    txt_to_say = ("сегодня солнечно")
    url_to_send = f"https://api.telegram.org/bot7074152795:AAFiS_4--4zHy6iWDv3VKbbzvCxB7iSPZ34/sendMessage?chat_id={chat_id}&text={txt_to_say}"
    requests.get(url_to_send)



