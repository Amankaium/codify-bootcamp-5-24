import telebot
from telebot import types

bot = telebot.TeleBot('6951830702:AAGdXJDi416NAV0Zy4k0cLaaw3LB8pMe_tI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message (message.chat.id, f'Привет, {message.from_user.username}')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message (message.chat.id, message)

@bot.message_handler(commands=['beast'])
def main(message):
    bot.send_message (message.chat.id, '<a> https://www.youtube.com/@MrBeast</a>', parse_mode='html')

@bot.message_handler(commands=[''])
def main(message):
    bot.send_message (message.chat.id, )

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton ('Лего')
    markup.row(btn1)
    btn2 = types.KeyboardButton ('Удалить фото')
    btn3 = types.KeyboardButton ('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, 'Message deleated')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton ('Лего', url = 'https://www.lego.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton ('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton ('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'вау', reply_markup = markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message (message.chat.id, f'Привет, {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')


bot.polling(none_stop=True)
