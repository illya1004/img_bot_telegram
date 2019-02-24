import config
import telebot
import os
from os import walk
import random

bot = telebot.TeleBot(config.token)

f = []
directory = 'img'
for (dirpath, dirnames, filenames) in walk(directory):
	f.extend(filenames)
	break

print(len(f))

@bot.message_handler(commands=['img'])
def send_photo(message):
	max_id_img = len(f) - 1
	img_random = random.randint(0, max_id_img)
	img = open("img/"+f[img_random],'rb')
	print(f[0])
	bot.send_photo(message.chat.id, img)

bot.polling()

while True:
	time.sleep(0)
