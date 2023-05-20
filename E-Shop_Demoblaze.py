from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

class Najdi_element():
    def klik(self):
        driver.maximize_window()
        driver.get("https://www.demoblaze.com/")
        driver.find_element(By.LINK_TEXT, "Laptops").click()

najdi_link = Najdi_element()
najdi_link.klik()