import telebot

with open("assets/bot-token.txt", "r") as f:
    token = f.read()

bot_username = "qwrtyzxcvbot"

bot = telebot.TeleBot(token, parse_mode=None, skip_pending=True)


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
