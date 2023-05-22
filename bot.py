import telebot
import val
import parcing
from telebot import types
bot = telebot.TeleBot('5724705081:AAF78TW5FNolA_e-t2PhiTR4i_1dHV8Ak0k')

url = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Добро пожаловать! Я бот для сокращения ссылок.')

@bot.message_handler(content_types=['text'])
def welcome(message):
    if message.text == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item = types.KeyboardButton("Сократить ссылку")
        keyboard.add(item)
        bot.send_message(message.from_user.id, "Нажмите кнопку", reply_markup = keyboard)
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')
        bot.register_next_step_handler(message, welcome)

@bot.message_handler(content_types=['text'])
def get_url(message):
    url = message.text
    if val.check_valid_url(url) == True:
        bot.send_message(message.from_user.id, 'Секундочку...')
        url = parcing.get_cut_url(url)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item = types.KeyboardButton("/start")
        keyboard.add(item)
        bot.send_message(message.from_user.id, text='Результат: ' + url, reply_markup = keyboard)
        bot.register_next_step_handler(message, welcome)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item = types.KeyboardButton("/start")
        keyboard.add(item)
        bot.send_message(message.from_user.id, 'Нерабочая ссылка', reply_markup = keyboard)
        bot.register_next_step_handler(message, welcome)
            
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Сократить ссылку':
        bot.send_message(message.from_user.id, "Пожалуйста, введите ссылку.")
        global url
        bot.register_next_step_handler(message, get_url)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item = types.KeyboardButton("Сократить ссылку")
        keyboard.add(item)
        bot.send_message(message.from_user.id, 'Неизвестная команда', reply_markup = keyboard)
        bot.register_next_step_handler(message, start)

bot.polling(none_stop=True, interval=0)
