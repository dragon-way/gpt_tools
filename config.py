import configparser
import os

start_message = ""
token = ""
url = ""
tag_human = ""
tag_ai = ""

config = configparser.ConfigParser()

def create_conf():
    global config
    config.add_section("Settings")
    config.set("Settings", "token", "***************************************")
    config.set("Settings", "start_message",
               "Приветствую тебя, кожанный! Я ChatGPT, искусственный интеллект от компании OpenAI. Можешь задавать мне вопросы! \n\nЕсли я затупил нажми /reboot.\n\nЕсли я тебе больше не отвечу значит я героически погиб...")
    config.set("Settings", "url", "https://chatgptt.me/")
    config.set("Settings", "tag_human", "wpaicg-chat-shortcode-typing")
    config.set("Settings", "tag_ai", "wpaicg-ai-message")
    with open("config.ini", "w", encoding="utf-8") as config_file:
        config.write(config_file)





def read_conf():
    if not os.path.exists("config.ini"):
        create_conf()

    global start_message
    global token
    global url
    global tag_human
    global tag_ai

    global config
    with open("config.ini", "r", encoding="utf-8") as config_file:
        config.read_file(config_file)


    start_message = config.get("Settings", "start_message")
    token = config.get("Settings", "token")
    url = config.get("Settings", "url")
    tag_human = config.get("Settings", "tag_human")
    tag_ai = config.get("Settings", "tag_ai")






