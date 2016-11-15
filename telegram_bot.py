#!/usr/bin/env python
import time
import telegram
import urllib.request
import ssl
from datetime import date
context = ssl._create_unverified_context()
page = urllib.request.urlopen('https://c.xkcd.com/random/comic/', context=context)
f = "Image URL (for hotlinking/embedding):"
s = str(page.read())
i = s.find(f)
j = s.find(".png", i)
count = 0

while((i == -1 or j == -1) and count < 50):
	page = urllib.request.urlopen('https://c.xkcd.com/random/comic/', context=context)	
	s = str(page.read())
	i = s.find(f)
	j = s.find(".png", i)
	count += 1
	time.sleep(10)

if (count < 50):	
	begin = i + 38
	end = j + 4
	#print (begin)
	#print (end)
	#print (s[begin:end])
	bot = telegram.Bot(token= "token")
	#print (bot.getMe())
	#chat_id = bot.getUpdates()[-1].message.chat_id
	bot.sendMessage(chat_id='@xkcdesto', text = str((date.today())))
	bot.sendPhoto(chat_id='@xkcdesto', photo=s[begin:end])
	
