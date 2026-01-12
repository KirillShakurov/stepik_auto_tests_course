from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)
    
    browser.execute_script("window.scrollBy(0, 150);")

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(result)

    chekbox = browser.find_element(By.ID, "robotCheckbox")
    chekbox.click()

    radioButton = browser.find_element(By.ID, "robotsRule")
    radioButton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
