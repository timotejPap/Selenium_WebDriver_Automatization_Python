from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


driver.get("https://predajne.kaufland.sk/")
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[@id='402r8Hptk8']").click()
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[contains(text(),'Povoliť vybrané')]").click()
time.sleep(3)

kontakt = driver.find_element(By.CLASS_NAME, "m-navigation-corporate__link").click()

print("Nazov stranky je: ", driver.title)