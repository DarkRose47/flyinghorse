# -*- coding: utf-8 -*-

import time
import telepot
from telepot.loop import MessageLoop


#handle fonksiyonu burada gelen mesajları yakalıyor
def handle(msg):
	chat_id = msg['chat']['id'] ##hangi chat id den geldiğini alıyor
	command = msg['text']## mesajın içeriğini okuyor
	whois = msg['from']['first_name']##burada ise kayıtlı adı çekiyor 

	print ('Got command: %s' % command)

	if command == '/rastgele':
		bot.sendMessage(chat_id, random.randint(1,100))
	elif command == '/merhaba':
		bot.sendMessage(chat_id,whois+' Merhaba' )
bot = telepot.Bot('TOKEN BURAYA YAZILACAK')
## handle fonksiyonunu mesajları devamlı yakalaması için thread olarak çalıştırıyoruz.
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')
#botumuzun durmaması içinde bir döngü içerisine alıyoruz
while 1:
    	time.sleep(10)
