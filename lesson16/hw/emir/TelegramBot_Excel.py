from excel_class import ExcelClass
from tgbot_class import TelegramBot
import time

TOKEN = "6843897717:AAFANiInEsvceqijMKdfL5nFWoG0mX6vcGU"
bot = TelegramBot(TOKEN)

excel_1 = ExcelClass("product.xlsx")

while True:
    chat_id, txt, message_id = bot.get_last_message()

    if message_id not in bot.answered:
        print(chat_id)

        if txt in ["1", "2", "3", "4", "5"]:
            product_num = int(txt) + 1

            response_txt = excel_1.read_row(product_num)
            bot.send_message(chat_id, response_txt)

            file_path = excel_1.read_row_photo(product_num)
            bot.send_photo(chat_id, file_path)

        if txt == "цены":
            response_txt = excel_1.get_pricelist()
            bot.send_message(chat_id, response_txt)

    bot.answered.append(message_id)
    time.sleep(1)
