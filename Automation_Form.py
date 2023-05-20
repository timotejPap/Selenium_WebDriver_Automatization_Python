import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
cookie = driver.find_element(By.ID, "ez-accept-necessary").click()

first_name = driver.find_element(By.NAME, "firstname").send_keys("Peter")
last_name = driver.find_element(By.NAME, "lastname").send_keys("Hric")
time.sleep(4)
#sex = driver.find_element(By.NAME, "sex").click()
#years_exp = driver.find_element(By.ID, "exp-0").click()
date = driver.find_element(By.ID, "datepicker").send_keys("20.5.2023")
profession = driver.find_element(By.ID, "profession-0").click()
profession = driver.find_element(By.ID, "profession-1").click()
profession = driver.find_element(By.ID, "tool-2").click()
continent_dropdown = driver.find_element(By.NAME, "continents")
dd = Select(continent_dropdown)
dd.select_by_visible_text("Europe")
