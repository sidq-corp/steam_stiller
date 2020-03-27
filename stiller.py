import time
import os
import telebot
import subprocess

token = ""

bot = telebot.TeleBot(token)
chat_id = 506563771
subprocess.check_call('start.bat', shell=True)


text = open('log.txt', 'rb')

bot.send_document(chat_id, text)