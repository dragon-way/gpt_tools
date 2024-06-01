import config
import telebot
import parser

config.read_conf()
parser.reboot()
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def starting(message):
    bot.send_message(message.chat.id, config.start_message)


@bot.message_handler(commands=["reboot"])
def starting(message):
    parser.reboot()
    bot.send_message(message.chat.id, "Я живой!")



@bot.message_handler(commands=["config"])
def starting(message):
    for s in config.config.read_string():
        print(s)
    bot.send_message(message.chat.id, "Я живой!")


@bot.message_handler(content_types=["text"])
def dialogue(message):
    parser.answer = ""
    parser.question = message.text
    while not parser.answer:
        pass
    bot.send_message(message.chat.id, parser.answer)



bot.polling(non_stop=True)
