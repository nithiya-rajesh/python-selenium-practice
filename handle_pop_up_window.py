from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.example.com")

#click on the link that opens a pop-up window
element=driver.find_element(By.LINK_TEXT("Open Pop_up"))
element.click()

# #get the window handles of all open windows
# handles=driver.window_handles

# #find the window handle dof the pop-up window
# pop_up_window_handle=handles[1]

# #switch the focus to the pop-up window

# driver.switch_to.window(pop_up_window_handle)

# #enter some text in the pop-up window

# driver.find_element(By.ID,"username").sendkey("myusername")

# #click on the sumbit button in the po-up window

# driver.find_element(By.ID, "submitButton").click()

driver.close()
