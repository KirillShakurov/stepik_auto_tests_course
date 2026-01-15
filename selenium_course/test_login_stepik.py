import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('lesson_link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])

def test_login_stepik(browser, lesson_link):
    link = lesson_link
    browser.get(link)

    login_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_button.click()

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_input.send_keys("kirill.shakurov@gmail.com")

    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys("110986Dik!")

    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn ").click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".sign-form"))
    )
    answer = str(math.log(int(time.time())))

    answer_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
    )

    answer_input.click()
    answer_input.clear()  # ← КРИТИЧНО: поле может содержать placeholder
    answer_input.send_keys(answer)
    time.sleep(2)
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )

    submit_button.click()
    time.sleep(3)

    feedback = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    message = feedback.text
    print(f"Фидбек урока: {message}")
    assert message == "Correct!", f"Инопланетное сообщение: '{message}' (ожидался 'Correct!')"

