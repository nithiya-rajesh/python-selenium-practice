# 1.Get Row and Column values from an HTML WebTable 

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.w3schools.com/html/html_tables.asp")

# Get the table element
table = driver.find_element(By.ID,("customers"))

# Get the number of rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")

# Get the number of columns in the table
columns = table.find_elements(By.TAG_NAME, "th")

# Print the row and column values
for row in rows:
    for column in columns:
        print(row.text, column.text)