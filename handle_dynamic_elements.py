from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.google.com/")

# find the first button element on the page that contains the text Google Search
Google_Search= driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("hello Google")
G_search= driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()

driver.quit()
