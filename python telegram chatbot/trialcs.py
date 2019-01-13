import telebot
import time
import messagehandler

API_TOKEN = '757772038:AAHYymvd3ofpGoK6M_RGZkhJFaf58GTyjlk'

bot = telebot.TeleBot(API_TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    insta_link = "https://instagram.com/{}".format(at_text[1:])



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    message_str = str(message.text)
    new_message = messagehandler.start(message_str)
    bot.reply_to(message, new_message.text)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


#757772038:AAHYymvd3ofpGoK6M_RGZkhJFaf48GTyjlk
