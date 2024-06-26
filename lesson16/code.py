import time
from excel_class import ExcelClass
from tg_class import TelegramBot


excel_1 = ExcelClass("product.xlsx")
# excel_1.read_row(3)

answered = []
telegram_bot = TelegramBot()
while True:
    chat_id, txt, message_id = telegram_bot.get_last_message()
    if message_id not in answered:
        print(chat_id)
        if txt in ["1", "2", "3", "4", "5"]:
            product_num = int(txt) + 1
            
            response_txt = excel_1.read_row(product_num)
            telegram_bot.send_message(chat_id, response_txt)
            
            file_path = excel_1.read_row_photo(product_num)
            telegram_bot.send_photo(chat_id, file_path)
            
    answered.append(message_id)
    time.sleep(1)
