from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.techwithtim.net/")
print(driver.title)

driver.get("https://www.selenium.dev/")
time.sleep(3)
print(driver.title)

driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)
