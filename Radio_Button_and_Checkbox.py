from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://letcode.in/radio")

buttons = driver.find_elements(By. CLASS_NAME, "control")
print("Length: ", len(buttons))

select = driver.find_element(By.ID, "yes").is_displayed()
print("Select: ", select)
select = driver.find_element(By.ID, "yes").is_selected()
print("Select: ", select)
select = driver.find_element(By.ID, "yes").click()
select = driver.find_element(By.ID, "yes").is_selected()
print("Select: ", select)

confirm_one = driver.find_element(By.ID, "one").click()
confirm_two = driver.find_element(By.ID, "two").click()
confirm_one = driver.find_element(By.ID, "one").is_selected()
confirm_two = driver.find_element(By.ID, "two").is_selected()
print("One: ", confirm_one)
print("Two: ", confirm_two)

nobug = driver.find_element(By.ID, "nobug").is_selected()
bug = driver.find_element(By.ID, "bug").is_selected()
print("Bug: ", nobug, bug)

nobug = driver.find_element(By.ID, "nobug").click()
bug = driver.find_element(By.ID, "bug").click()

nobug = driver.find_element(By.ID, "nobug").is_selected()
bug = driver.find_element(By.ID, "bug").is_selected()
print("Bug", nobug, "Bug", bug)

foo = driver.find_element(By.ID, "foo").is_selected()
bar = driver.find_element(By.ID, "notfoo").is_selected()
print("Foo: ", foo, bar)

enabled = driver.find_element(By.ID, "maybe").is_enabled()
print("Disabled: ", enabled)

checkbox = driver.find_element(By. XPATH, "//label[normalize-space()='Remember me']//input[@type='checkbox']").is_selected()
print("Checkbox is: ", checkbox)