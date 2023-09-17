# 7. How to mouse hover over a web element? 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.google.com/")

#find the search input box
search_box= driver.find_element(By.ID,"APjFqb")

#mouse over the search box
act=ActionChains(driver)
act.move_to_element(search_box).send_keys("google").perform()

driver.close()