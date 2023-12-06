import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_failed_login(self):  # test cases 1
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("haitest")
        driver.find_element(By.ID, "password").send_keys("haitest")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn(
            "Epic sadface: Username and password do not match any user in this service",
            error_message,
        )

    def test_success_login(self):  # test cases 2
        url = "https://www.saucedemo.com/"
        driver = self.browser
        driver.get(url)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(
            "secret_sauce"
        )
        driver.find_element(By.NAME, "login-button").click()
        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = driver.current_url
        self.assertEqual(
            current_url, expected_url, "Failed to navigate to the inventory page."
        )


if __name__ == "__main__":
    unittest.main()