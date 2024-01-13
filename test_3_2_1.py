import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegister:
    def test_register1(self):
        browser = webdriver.Chrome()

        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first:required')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second:required')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third:required')
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, 'Ok'

    def test_register2(self):
        browser = webdriver.Chrome()

        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first:required')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second:required')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third:required')
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, 'Ok'


if __name__ == "__main__":
    pytest.main()
