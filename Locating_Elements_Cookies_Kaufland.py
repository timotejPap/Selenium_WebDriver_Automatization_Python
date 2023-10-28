from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Toto ponechá okno otvorené
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Kódenie automatizácie
driver.get("https://www.kaufland.sk/")
driver.maximize_window()
time.sleep(5)

cookie = driver.find_element(By.ID, "onetrust-reject-all-handler").click()
time.sleep(3)
print("Nazov webu je: ", driver.title)


search = driver.find_element(By.NAME, "search_value")
time.sleep(5)
submit = driver.find_element(By.XPATH, "//button[@type='button']//span[@class='svg-icon']//*[name()='svg']")
ActionChains(driver).send_keys_to_element(search, "slanina").click(submit).perform()
time.sleep(4)
slane = driver.find_element(By.XPATH, "//div[contains(text(),'Slané pečivo')]").click()
odkaz = driver.find_element(By.CLASS_NAME, "rd-footer_navigation-link-list-item").click()
print(driver.title)