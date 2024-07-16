import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import requests
from bs4 import BeautifulSoup

url = 'https://catalogo.movistar.com.pe/?_ga=2.203970004.513691793.1708499701-2017598126.1708499701'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

href_values = []
div_tags = soup.find_all('div', class_='__column')
for div_tag in div_tags:
    a_tags = div_tag.find_all('a')
    href_values.extend([a.get('href') for a in a_tags])

# Check if the Excel file exists, create it if it doesn't
file_path = 'movistar_peru.xlsx'
if not os.path.exists(file_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Price"])
    wb.save(file_path)
else:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

# Start the WebDriver
driver = webdriver.Chrome()

for url in href_values[96:]:
    # Open the webpage
    driver.get(url)

    # Wait for the memory buttons to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_memory')))

    # Find all memory buttons
    memory_buttons = driver.find_elements(By.CLASS_NAME, 'js_memory')

    for memory_button in memory_buttons:
        # Click the memory button if it's not already active
        if 'active' not in memory_button.get_attribute('class'):
            memory_button.click()

            # Wait for the button to become active
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_memory.active')))

        # Get the memory, device name, and price
        memory = memory_button.text
        try:
            device_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'inner'))).text
            price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_price_cash'))).text

            # Concatenate device name and memory to form final name
            final_name = f"{device_name} {memory}"

            # Append the data to the Excel sheet
            ws.append([final_name, price])
            wb.save(file_path)  # Save the Excel file after each record is extracted
        except Exception as e:
            print(f"Error getting device name and price: {e}")

# Close the WebDriver
driver.quit()
