import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions

import config

options = EdgeOptions()
options.add_argument("InPrivate")
options.add_argument("--headless")


question = ""
answer = ""
thread = None
work_flag = True


def wb():
    global options

    global question
    global answer
    browser = webdriver.Edge(options=options)
    browser.get(url=config.url)
    time.sleep(5)

    while work_flag:
        if question:
            try:
                q = browser.find_element(By.CLASS_NAME, config.tag_human
                                         )
                q.send_keys(question)
                time.sleep(1)
                q.send_keys(Keys.ENTER)
                print("keys")
                time.sleep(1)

                #waiting 1 step
                processing = browser.find_element(By.CLASS_NAME, "wpaicg-bot-thinking")
                while processing.is_displayed():
                    print("processing")
                time.sleep(1)

                #waiting 2 step
                len_answer = 0
                while len_answer != len(browser.find_elements(By.CLASS_NAME, config.tag_ai)[-1].text):
                    print("printing")
                    len_answer = len(browser.find_elements(By.CLASS_NAME, config.tag_ai)[-1].text)
                    time.sleep(1)

                answer = browser.find_elements(By.CLASS_NAME, config.tag_ai)[-1].text
                question = ""

            except Exception as e:
                print(e)
                question = ""


def reboot():
    global thread
    global work_flag
    work_flag = False
    time.sleep(1)
    thread = threading.Thread(target=wb)
    thread.daemon = True
    work_flag = True
    thread.start()
