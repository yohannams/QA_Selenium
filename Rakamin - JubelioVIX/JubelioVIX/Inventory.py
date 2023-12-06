import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import BaseLogin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            ChromeDriverManager(version="114.0.5735.90").install()
        )

    def test_a_success_atur_stok_persediaan(self):
        # steps
        driver = self.browser  # buka web browser
        BaseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='wrapper']/nav[@class='navbar-default navbar-static-side']//div[@class='metismenu nav']/ul[@class='metismenu-container']/li[2]/a[@href='#']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='wrapper']/nav[@class='navbar-default navbar-static-side']//div[@class='metismenu nav']/ul[@class='metismenu-container']//ul[@class='metismenu-container visible']//a[@href='/home/inventory']/span[.='Persediaan']",
        ).click()
        time.sleep(2)
        response_data = driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[2]/div[@class='col-lg-12']//h1[.='Persediaan']",
        )
        self.assertIn("Persediaan", response_data.text)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/home/inventory/"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='ibox']/div[@class='ibox-content']/div[@class='row']//div[@class='pull-right']/button[2]/span[@class='ladda-label']",
        ).click()
        time.sleep(1)

        element = driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']/div[2]//div[@class='react-grid-Row react-grid-Row--even']/div[1]//span[@class='text-muted']",
        )
        # Inisialisasi objek ActionChains
        action_chains = ActionChains(driver)
        # Lakukan double-click pada elemen
        action_chains.double_click(element).perform()
        time.sleep(2)
        driver.find_element(
            By.CLASS_NAME,
            "selectivity-single-select",
        )
        time.sleep(1)
        driver.find_element(
            By.CLASS_NAME,
            "selectivity-search-input",
        ).send_keys("vivo")
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR,
            'div[data-item-id="216"]',
        ).click()
        time.sleep(2)
        inputan = driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']//div[@class='react-grid-Row react-grid-Row--even']/div[2]//div[@title='1']",
        )
        # Inisialisasi objek ActionChains
        action_chains = ActionChains(driver)
        # Lakukan double-click pada elemen
        action_chains.double_click(inputan).perform()
        qty = driver.find_element(
            By.XPATH,
            "//body[@id='page-top']//div[@class='rdg-editor-container']/input[@value='1']",
        ).send_keys("100")
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']/div/div[1]//label[.='Note: Harga Pokok hanya bisa diubah untuk penyesuaian (+)']",
        ).click()
        driver.find_element(
            By.XPATH,
            "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']//div[@class='react-grid-Row react-grid-Row--even']/div[@value='100']//div[@title='100']/div[@class='text-right']",
        ).click()
        self.assertIn(
            "100",
            driver.find_element(
                By.XPATH,
                "//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']//div[@class='react-grid-Row react-grid-Row--even']/div[@value='100']//div[@title='100']/div[@class='text-right']",
            ).text,
        )
        time.sleep(1)
        driver.find_element(
            By.CLASS_NAME,
            "ladda-button",
        ).click()
        time.sleep(5)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
