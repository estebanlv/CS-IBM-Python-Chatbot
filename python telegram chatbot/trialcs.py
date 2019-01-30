import telebot
import time
import messagehandler

API_TOKEN = '757772038:AAHYymvd3ofpGoK6M_RGZkhJFaf58GTyjlk'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am the IBM Helpbot.
This is the list of commands you can use to navigate this bot:
/start: show the introduction of the bot.
/help: get a list of commands to navigate the bot.\
""")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am the IBM Helpbot.
I am here to help you find any Cloud product from IBM's catalog. Just tell me what you are serching for
and I will do my best to find it for you.\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    message_str = str(message.text)
    print(message_str)
    print(message.from_user.id)
    new_message = messagehandler.start(message_str)
    #bot.reply_to(message, new_message.text)
    #bot.send_message(message.from_user.id, "I think this might help you.")
    #bot.reply_to(message, new_message)
    if new_message == "Sorry but your request was unsuccesful, please try again":
        bot.send_message(message.from_user.id, new_message)
    else:
        bot.send_message(message.from_user.id, "I think this might help you.")
        bot.send_message(message.from_user.id, new_message)
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


#757772038:AAHYymvd3ofpGoK6M_RGZkhJFaf48GTyjlk
