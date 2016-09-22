import sys
import time
import telepot


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		bot.sendMessage(chat_id, msg['text'])
# End of handle()

token = "241230209:AAFqNOg0o2RXObN2sk1LnQUU71cQkr50MO4"

bot = telepot.Bot(token)
bot.message_loop(handle)
print('listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
