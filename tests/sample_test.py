# Python program to demonstrate selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# create webdriver object
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# get google.co.in
driver.get("https://LinkedIn.com/login")
driver.maximize_window()

# Locate and interact with the login elements
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//*[@type='submit']")

# Enter login credentials and submit the form
username_field.send_keys("your_username")
password_field.send_keys("your_password")
login_button.click()


time.sleep(20)
print(driver.title)
print(driver.current_url)
driver.quit()

# Run this file by IDE

