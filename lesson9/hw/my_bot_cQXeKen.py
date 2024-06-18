a = '''
— Я сразу сказала татуировщику что я натура тонкая, характер изменчивый, поэтому мне нужно что-то особенное. Мы несколько часов перебирали варианты, обсуждали нюансы, спорили…
— Что в итоге он тебе набил?
— Морду!
'''
b = '''Если с первого раза у вас ничего не получилось – парашютный спорт не для вас!..'''
c = '''
– Что вы будете делать, если увидите зеленого человечка?
60% ответили – брошу пить!
30% – начну пить!
9% – пойду на прием к психиатру!
И только одна девушка сказала: «Начну переходить дорогу!»
'''
d = '''
Мой младший брат-первоклассник каждое утро сам ездит на 148-м троллейбусе в 1326-ю школу, где его учат считать до десяти.
'''
e = '''
Урок на дистанционке. Учитель:
— Кто будет отвечать?
Класс:
— …
Учитель:
— Лес рук. Тогда пойдем по алфавиту, отвечать будет AngryKitty2008.
'''

spisok = []
spisok.append(a)
spisok.append(b)
spisok.append(c)
spisok.append(d)
spisok.append(e)

import random
import requests


url = "https://api.telegram.org/bot6703866816:AAF-ZnApVh6DNWm5_V1mhl2xSYg4VQrrjC0/getUpdates"
response = requests.get(url)
data = response.json()  # json == dictionary
txt = data["result"][-1]["message"]["text"]

city = 'Бишкек'
url_1 = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url_1).json()
temperature = round(weather_data['main']['temp'])

def anecdot_weather(txt):
    if txt == "say a joke":
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        txt_to_say = random.choice(spisok)
        url_to_send = f"https://api.telegram.org/bot6703866816:AAF-ZnApVh6DNWm5_V1mhl2xSYg4VQrrjC0/sendMessage?chat_id={chat_id}&text={txt_to_say}"
        requests.get(url_to_send)
    elif txt == "weather":
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        txt_to_say = str(temperature) + '°C'
        url_to_send = f"https://api.telegram.org/bot6703866816:AAF-ZnApVh6DNWm5_V1mhl2xSYg4VQrrjC0/sendMessage?chat_id={chat_id}&text={txt_to_say}"
        requests.get(url_to_send)

anecdot_weather(txt)
