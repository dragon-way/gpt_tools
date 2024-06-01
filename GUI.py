import customtkinter
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions


options = EdgeOptions()
options.add_argument("InPrivate")
options.add_argument("--headless")

url = "https://chatgptt.me/"

question = ""
answer = ""

thread = None
stop_flag = False


def vopros(event):
    global question
    question = entry.get()
    text_box.insert("end", "\nВопрос\n" + entry.get() + "\n")
    entry.delete(0, "end")


def wb():
    global options
    global answer
    global question

    browser = webdriver.Edge(options=options)
    browser.get(url=url)
    time.sleep(1)
    print("браузер запущен")
    entry.configure(state="normal")
    entry.configure(placeholder_text_color="green")
    entry.configure(placeholder_text="Напишите вопрос....")

    app.configure(fg_color="green")
    while not stop_flag:
        time.sleep(1)
        if question:
            try:
                q = browser.find_element(By.CLASS_NAME, "wpaicg-chat-shortcode-typing")
                q.send_keys(question)
                time.sleep(1)
                q.send_keys(Keys.ENTER)
                time.sleep(20)

                # тормозим выполнение кода дальше
                processing = browser.find_element(By.CLASS_NAME, "wpaicg-bot-thinking")
                while processing.is_displayed():
                    print("думаю......")

                len_answer = 0
                real_len_answer = len(browser.find_elements(By.CLASS_NAME, "wpaicg-ai-message")[-1].text)
                while len_answer != real_len_answer:
                    len_answer = real_len_answer
                    print("печатаю.....")

                answer = browser.find_elements(By.CLASS_NAME, "wpaicg-ai-message")[-1].text
                print(answer)
                text_box.insert("end", "\nОтвет\n" + answer[4:] + "\n")
                text_box.see("end")
                question = ""
                answer = ""
            except Exception as error:
                print(error)
                question = ""
                answer = ""
    print("end def")


thread1 = threading.Thread(target=wb)
thread1.start()


def finish():
    global stop_flag
    stop_flag = True
    app.destroy()


app = customtkinter.CTk()

entry = customtkinter.CTkEntry(app, font=("comicsans", 40), width=600, fg_color="black", border_color="black",
                               text_color="green", placeholder_text="Загрузка...............", placeholder_text_color="green")
entry.pack(padx=20, pady=10)

entry.configure(state="disabled")
entry.bind("<Return>", vopros)

text_box = customtkinter.CTkTextbox(app, font=("comicsans", 40), width=600, fg_color="black", border_color="black",
                                    text_color="green", height=800)
text_box.pack(padx=20, pady=10)




app.protocol("WM_DELETE_WINDOW", finish)
app.mainloop()
