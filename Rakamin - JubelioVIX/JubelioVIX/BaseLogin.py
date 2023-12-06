import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_a_success_login(driver):
    # steps
    driver.get("https://app.jubelio.com/")  # buka situs
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "ladda-button").click()
    time.sleep(5)
