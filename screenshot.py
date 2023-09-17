from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os


#create a WebDriver instance
driver = webdriver.Firefox()

#navigate to the web page you want to take a screenshot of 
driver.get("https://www.pizzagpt.it/")
driver.maximize_window()

# create a webdriverscreenshot object
driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()
