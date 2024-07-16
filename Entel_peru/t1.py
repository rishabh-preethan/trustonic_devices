from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

# Path to your webdriver executable
url = 'https://miportal.entel.pe/personas/catalogo/postpago/renovacion?_ga=2.80071444.262870764.1709553476-1068951968.1709553452'

# Initialize the webdriver
driver = webdriver.Chrome()
driver.get(url)

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Brand', 'Model', 'Price'])

while True:
    # Find elements for brand, model, and price
    brand_elements = driver.find_elements(By.CLASS_NAME, 'product-brand')
    model_elements = driver.find_elements(By.CLASS_NAME, 'product-name')
    price_elements = driver.find_elements(By.CLASS_NAME, 'spot-price')

    # Iterate over the elements and extract text
    for brand_element, model_element, price_element in zip(brand_elements, model_elements, price_elements):
        brand = brand_element.text
        model = model_element.text
        price = price_element.text
        ws.append([brand, model, price])

    # Click on the "Load More" button
    try:
        load_more_button = driver.find_element(By.CLASS_NAME, 'page-right')
        load_more_button.click()
        # Wait for some time to load more content
        time.sleep(2)
    except:
        # If the "Load More" button is not found, break the loop
        break

# Save the Excel file
wb.save('Entel_peru/entel_peru.xlsx')

# Close the webdriver
driver.quit()
