from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(
    "--user-data-dir=" + os.path.join(dir_path, "profile", "whatsapp"))
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://web.whatsapp.com/')


time.sleep(15)


def bot():
    try:
        noti = driver.find_elements(By.CLASS_NAME, 'x173ssrc')
        last_noti = noti[-1]
        noti_action = webdriver.common.action_chains.ActionChains(driver)
        noti_action.move_to_element_with_offset(last_noti, 0, -20)
        noti_action.click()
        noti_action.perform()
        noti_action.click()
        noti_action.perform()
        time.sleep(5)
    except:
        print('buscando novas notificações')


while True:
    bot()
