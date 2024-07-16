from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Path to your webdriver executable
url = 'https://www.att.com.mx/planes/armalo-cotizador.html'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)  # Wait for the page to load
# Click the "See more products" button until there are no more devices
while True:
    try:
        show_more_button = driver.find_element(By.CLASS_NAME, 'js-show-more-product')
        show_more_button.click()
        time.sleep(5)  # Wait for new devices to load
    except:
        break 

# Find elements for name and price
name_elements = driver.find_elements(By.CLASS_NAME, 'pdp-link')
price_elements = driver.find_elements(By.CLASS_NAME, 'sales')

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Name'])

# Extract text for name and price
for name_element, price_element in zip(name_elements, price_elements):
    name = name_element.find_element(By.TAG_NAME, 'a').text
    price = price_element.text
    ws.append([name])

# Save the Excel file
wb.save('att_mx_built_phy_store.xlsx')

# Close the webdriver
driver.quit()
