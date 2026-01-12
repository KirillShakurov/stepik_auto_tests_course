from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)
    print(result)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()


finally:
    time.sleep(10)
    browser.quit()
