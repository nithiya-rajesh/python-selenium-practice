from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# create a selenium webdriver instance
driver = webdriver.Firefox()

# navigate to the page with the dropdown element
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

# create a Select object for the dropdown
select = Select(driver.find_element(By.CSS_SELECTOR,"select[name='continents']"))

# select the "Europe" option
select.select_by_visible_text("Europe")

# close the browser
driver.quit()