import requests


class TelegramBot:
    token = "7462059310:AAGeGQTueeN5B-aLx1FjqwiIOBoupJ5yg7k"
    base_url = f"https://api.telegram.org/bot{token}"

    def get_last_message(self):
        url = self.base_url + "/getUpdates"
        response = requests.get(url)
        data = response.json()  # json == dictionary
        txt = data["result"][-1]["message"]["text"]
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        message_id = data["result"][-1]["message"]["message_id"]
        return chat_id, txt, message_id
    
    def send_message(self, chat_id, txt):
        url_to_send = f"{self.base_url}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": txt
        }
        requests.get(url_to_send, params=params)
    
    def send_photo(self, chat_id, fl):
        url_to_send = f"{self.base_url}/sendPhoto"
        params = {
            "chat_id": chat_id,
        }
        files = {"photo": fl}
        requests.get(url_to_send, params=params, files=files)
