import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
cookie = driver.find_element(By.ID, "ez-accept-all").click()
wait = WebDriverWait(driver, 30)

female = driver.find_element(By. ID, "sex-1").is_selected()
print(female)

time.sleep(10)
driver.find_element(By. XPATH, "//input[@id='sex-1']").click()
female = driver.find_element(By. ID, "sex-1").is_selected()
print(female)
