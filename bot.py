import os
from telebot import telebot
from config import TOKEN
from telebot.util import quick_markup
from config import DATABASE
from logic import info





token = TOKEN
bot = telebot.TeleBot(token)
button_data = {
        'hor1e': {'callback_data':'author'},
        'projects': {'callback_data':'projects'},
        'GitHub':{"url":'https://github.com/Hor1e'}

        }
markup = quick_markup(button_data, row_width=2)


@bot.message_handler(commands=["start"])
def privet(message):
    global markup
    bot.send_message(message.chat.id, "Добро пожаловать! Я - бот-портфолио. Что конкретно тебе интересно.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'author')
def handle_back_callback(call):
    bot.answer_callback_query(call.id, text="...")
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Я - Python разработчик. Что дальше?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'projects')
def handle_back_callback(call):
        
    bot.answer_callback_query(call.id, text="...")
    
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Вот мои проекты:\n\n{info}\n\nЧто дальше?", reply_markup=markup)


    

    


bot.infinity_polling()


