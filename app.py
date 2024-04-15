from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from openai import OpenAI
client = OpenAI()

dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(
    "--user-data-dir=" + os.path.join(dir_path, "profile", "whatsapp"))
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://web.whatsapp.com/')


time.sleep(15)


def bot():
    try:
        # PROCURANDO NOTIFICAÇÃO
        time.sleep(5)
        noti = driver.find_elements(By.CLASS_NAME, 'x173ssrc')
        last_noti = noti[-1]
        noti_action = webdriver.common.action_chains.ActionChains(driver)
        noti_action.move_to_element_with_offset(last_noti, 0, -20)
        noti_action.click()
        noti_action.perform()
        noti_action.click()
        noti_action.perform()

        # CLASS_NAME _akbu
        all_msg = driver.find_elements(By.CLASS_NAME, '_akbu')
        all_text_msg = [e.text for e in all_msg]
        msg = all_text_msg[-1]
        print(msg)
        time.sleep(5)

        # XPATH //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p
        text_field = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        text_field.click()
        time.sleep(3)
        text_field.send_keys('bot-wpp', Keys.ENTER)
        time.sleep(2)

        # FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except:
        print('buscando novas notificações')


while True:
    bot()
