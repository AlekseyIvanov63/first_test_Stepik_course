from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import math
import time


answer = math.log(int(time.time()))


load_dotenv()

browser = webdriver.Chrome()
#url1 = #'https://stepik.org/lesson/236895/step/1'
        #'https://stepik.org/lesson/236896/step/1'
        #'https://stepik.org/lesson/236897/step/1',
        #'https://stepik.org/lesson/236898/step/1',
        #'https://stepik.org/lesson/236899/step/1',
        #'https://stepik.org/lesson/236903/step/1',
        #'https://stepik.org/lesson/236904/step/1',
        #'https://stepik.org/lesson/236905/step/1'


def test_poisk():
    browser.get('https://stepik.org/lesson/236905/step/1')
    browser.delete_all_cookies()
    browser.implicitly_wait(10)
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(os.getenv('login'))
    browser.find_element(By.ID, 'id_login_password').send_keys(os.getenv('passw'))
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader ').click()
    sleep(3)
    browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    sleep(3)
    value = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    item = value.text
    assert "Correct!" == item