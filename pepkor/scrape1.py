from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

# List of links to iterate over
links = [
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=1",
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=2",
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=3",
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=4",
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=5",
    "https://www.incredible.co.za/products/cellphones-wearables/cellphones?p=6"
]

# Path to your webdriver executable
driver = webdriver.Chrome()

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Name', 'Price'])

for link in links:
    driver.get(link)
    time.sleep(3)
    name_elements = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    price_elements = driver.find_elements(By.CLASS_NAME, 'price')

    # Extract text for name and price
    for name_element, price_element in zip(name_elements, price_elements):
        name = name_element.text.strip()
        price = price_element.text.strip()
        ws.append([name, price])

# Save the Excel file
wb.save('pepkor//pepkor1.xlsx')

# Close the webdriver
driver.quit()
