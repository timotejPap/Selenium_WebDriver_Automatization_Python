from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://orteil.dashnet.org/cookieclicker/")
pop_up = driver.find_element(By.CLASS_NAME, "fc-button-label").click()
time.sleep(5)

pop_up = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN").click()
time.sleep(5)

actions = ActionChains(driver)
cookie_clicker = driver.find_element(By.ID, "bigCookie")
#clicker_count = driver.find_element(By.ID, "cookies")
actions.double_click(cookie_clicker).perform()
items = driver.find_element (By.ID ("productPrice" + str(1))
for i in range(1, -1, -1))

for i in range(5000):
    actions.perform()