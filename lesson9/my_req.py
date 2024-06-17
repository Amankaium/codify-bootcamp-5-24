# pip install requests
# pip freeze
import requests

# response = requests.get("https://habr.com/ru/news/822167/")
# print(response.text)  # html-код

url = "https://api.telegram.org/bot7462059310:AAGeGQTueeN5B-aLx1FjqwiIOBoupJ5yg7k/getUpdates"
response = requests.get(url)
data = response.json()  # json == dictionary
txt = data["result"][-1]["message"]["text"]
print(txt)

if txt == "say hello":
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    txt_to_say = "hello world"
    url_to_send = f"https://api.telegram.org/bot7462059310:AAGeGQTueeN5B-aLx1FjqwiIOBoupJ5yg7k/sendMessage?chat_id={chat_id}&text={txt_to_say}"
    requests.get(url_to_send)
