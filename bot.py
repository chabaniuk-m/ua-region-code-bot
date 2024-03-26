import telebot

token = "6120494325:AAHhciagA8yFnQ904VLPFmZSwMC4E3WKdd8"
bot_username = "qwrtyzxcvbot"

bot = telebot.TeleBot(token, parse_mode=None)


is_reply = True


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['stop'])
def stop_echo(message):
    global is_reply
    is_reply = False


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if is_reply:
        bot.reply_to(message, message.text)


bot.infinity_polling()
