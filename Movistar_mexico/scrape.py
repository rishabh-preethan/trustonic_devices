from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://tienda.movistar.com.mx/terminales.html')

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Name', 'Price'])

# Function to extract data from the current page and store in Excel
def extract_data_and_store():
    names = driver.find_elements(By.CLASS_NAME, 'grid__title')
    prices = driver.find_elements(By.CLASS_NAME, 'grid__terminal-pospago-precio')
    
    for name, price in zip(names, prices):
        ws.append([name.text, price.text])
        print(name.text, price.text)

# Extract data from the first page and store in Excel
extract_data_and_store()

# Loop to navigate to the next page, extract data, and append to Excel
while True:
    try:
        next_page_button = driver.find_element(By.CLASS_NAME, 'vass-page-next')
        next_page_link = next_page_button.get_attribute('href')
        if next_page_link:
            driver.get(next_page_link)
            time.sleep(5)  # Wait for the page to load
            extract_data_and_store()
        else:
            break  # If no next page link is found, exit the loop
    except Exception as e:
        print("Error navigating to the next page:", e)
        break

# Save the Excel file
wb.save('Movistar_mexico//movistar_mexico_renewal.xlsx')

# Close the WebDriver
driver.quit()
