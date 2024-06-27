import requests


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.answered = []

    def get_last_message(self):
        url = self.base_url + "/getUpdates"
        response = requests.get(url)
        data = response.json()
        txt = data["result"][-1]["message"]["text"]
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        message_id = data["result"][-1]["message"]["message_id"]
        return chat_id, txt, message_id

    def send_message(self, chat_id, txt_to_say):
        url_to_send = f"{self.base_url}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": txt_to_say,
            "disable_web_page_preview": True
        }
        requests.get(url_to_send, params=params)

    def send_photo(self, chat_id, fl):
        binary_file = fl
        url_to_send = f"{self.base_url}/sendPhoto"
        params = {
            "chat_id": chat_id,
            "photo": binary_file
        }
        requests.get(url_to_send, params=params)
