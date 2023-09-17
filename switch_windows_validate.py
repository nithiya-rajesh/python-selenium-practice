from selenium import webdriver
urlA = "https://www.tutorialspoint.com/about/about_careers.htm"
urlB = "https://www.tutorialspoint.com/questions/index.php"
driver = webdriver.Firefox()
# opening another driver session
s_driver = webdriver.Firefox()
# maximize with maximize_window()
driver.maximize_window()
s_driver.maximize_window()
driver.get(urlA)
s_driver.get(urlB)
print(driver.title)
print(s_driver.title)
driver.quit()