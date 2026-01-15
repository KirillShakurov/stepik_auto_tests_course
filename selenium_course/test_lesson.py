import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Заполняем обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Kirill")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Shakurov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("shakurov@gmail.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Заполняем обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Kirill")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Shakurov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("shakurov@gmail.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
