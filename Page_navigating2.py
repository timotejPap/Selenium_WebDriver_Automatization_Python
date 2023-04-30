from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


driver.get("https://www.techwithtim.net/")
print("Toto je nazov stranky:", driver.title)

link = driver.find_element(By.LINK_TEXT, "Python Programming").click()
time.sleep(5)

link = driver.find_element(By.LINK_TEXT, "Beginner Python Tutorials").click()

link = driver.find_element(By.ID, "sow-button-19310003").click()

driver.back()