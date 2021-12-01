import os
import telebot
from decouple import config

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ["Greet"])
def greet(message):
    bot.reply_to(message, "Oi, tudo bem?")

@bot.message_handler(commands = ["olá"])
def test(message):
    bot.send_message(message.chat.id, "Olá")

@bot.message_handler(regexp = "twitch.tv/steph")
def change(message):
    bot.set_chat_title(message.chat.id, "Teste")

    

bot.polling()
