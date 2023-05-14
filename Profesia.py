import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


browser.get("https://www.profesia.sk/")
cookie = browser.find_element(By. ID, "CybotCookiebotDialogBodyButtonDecline").click()
browser.find_element(By. ID, "offerCriteriaSuggesterInputId").send_keys("IT tester")
submit = browser.find_element(By. ID, "offer-search-link").click()