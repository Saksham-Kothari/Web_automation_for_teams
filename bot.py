import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/ChromeDriver"
driver = webdriver.Chrome()

my_user_name = "standard_user"
my_password = "secret_sauce"

# Opens the URL page
driver.get("https://www.saucedemo.com/")

driver.implicitly_wait(5)  # wait for 3 sec after loading browser

try:
    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
except:
    print("No elements with this Id name")

user_name.send_keys(my_user_name)
password.send_keys(my_password)

try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "user-name"), "standard_user ")
    )
finally:
    login_button.click()
