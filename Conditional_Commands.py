from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)

driver.get("https://selectorshub.com/xpath-practice-page/")
email_input = driver.find_element(By.ID, "userId")

print(email_input.is_displayed())
print(email_input.is_displayed())

password_input = driver.find_element(By.ID, "pass")
print(password_input.is_displayed())

company_input = driver.find_element(By. NAME, "company")
email_input.send_keys("jozko@mrkvicka.sk")
password_input.send_keys("123456789")
company_input.send_keys("Rodinkarstvo")
submit = driver.find_element(By. XPATH, "/html/body/div[1]/main/div/div[1]/section[2]/div/div[1]/div/div[1]/div/form/div/input[3]").click()



driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
cookie = driver.find_element(By.ID, "ez-accept-all").click()
time.sleep(5)
male = driver.find_element(By.ID, "sex-0").click()
radio_button = driver.find_element(By.ID, "sex-0")
print(radio_button.is_selected())