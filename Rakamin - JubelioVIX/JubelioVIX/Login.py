import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            ChromeDriverManager(version="114.0.5735.90").install()
        )

    def test_a_success_login(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://app.jubelio.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "email").send_keys(
            "qa.rakamin.jubelio@gmail.com"
        )  # isi email
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(
            "Jubelio123!"
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ladda-button").click()
        time.sleep(5)

        # validasi
        driver.find_element(By.CLASS_NAME, "side-logo")

    def test_a_failed_login_wrong_input(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://app.jubelio.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "email").send_keys("user@example.com")  # isi email
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ladda-button").click()

        # validasi
        wait = WebDriverWait(driver, 5)
        element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
        )  # eksplisit wait
        self.assertIn("Password atau email anda salah.", element.text)

    def test_a_failed_login_empty_password(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://app.jubelio.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "email").send_keys("user@example.com")  # isi email
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ladda-button").click()
        # validasi
        wait = WebDriverWait(driver, 5)
        element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
        )  # eksplisit wait
        self.assertIn("Password harus diisi.", element.text)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
