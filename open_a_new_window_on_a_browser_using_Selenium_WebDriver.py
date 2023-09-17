from selenium import webdriver

urlA= "https://testpages.eviltester.com/styled/basic-web-page-test.html"
urlB= "https://testpages.eviltester.com/styled/attributes-test.html"

driver=webdriver.Firefox()
s_driver=webdriver.Firefox()

driver.maximize_window()
s_driver.maximize_window()

driver.get(urlA)
s_driver.get(urlB)

print(driver.title)
print(s_driver.title)

driver.quit()


