import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Testart(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_cart(self):  # test cases 1
        url = "https://www.saucedemo.com/"
        driver = self.browser
        driver.get(url)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(
            "secret_sauce"
        )
        driver.find_element(By.NAME, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.assertIn(
            "Sauce Labs Backpack",
            driver.find_element(By.CLASS_NAME, "inventory_item_name").text,
        )


if __name__ == "__main__":
    unittest.main()