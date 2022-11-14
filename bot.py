import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sqlite3

os.environ['PATH'] += r"C:/ChromeDriver"
driver = webdriver.Chrome()

my_email_id = "mohit.laxminarayan2021@vitbhopal.ac.in"
my_password = "Mohit@461981"

# Opens the URL page
driver.get("https://teams.microsoft.com")
time.sleep(3)

# driver.implicitly_wait(3)  # wait for 3 sec after loading browser


def login():

    global driver
    # Enter Eamil ID
    time.sleep(2)
    email_field = driver.find_element(By.ID, "i0116")
    email_field.send_keys(my_email_id)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(3)
    # Enter Password
    password_field = driver.find_element(By.ID, "i0118")
    password_field.send_keys(my_password)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(3)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    driver.find_element(
        By.ID, "app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c").click()


def create_DB():
    connection = sqlite3.connect('timetable.db')
    cursor = connection.cursor()
    cursor.execute(
        '''CREATE TABLE timetable(class text, start_time text, end_time text, day text)''')
    connection.commit()
    connection.close()
    print("Time table created!")


login()
