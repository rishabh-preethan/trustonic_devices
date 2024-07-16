from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

# Path to your webdriver executable
driver = webdriver.Chrome()

# URL of the website to extract details from
url = 'https://ww2.movistar.cl/ofertas/equipo-plan/'
# url = 'https://ww2.movistar.cl/ofertas/renovacion-movil/boleta/'
url = 'https://ww2.movistar.cl/ofertas/celulares-liberados/'
url = 'https://ww2.movistar.cl/ofertas/renovacion-movil/tarjeta/'
# url = 'https://ww2.movistar.cl/ofertas/seminuevos/'
# url = 'https://ww2.movistar.cl/ofertas/accesorios/'
driver.get(url)
time.sleep(15)
# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Name', 'Price'])

# Find elements for name and price
name_elements = driver.find_elements(By.CLASS_NAME, 'of-card-name')
price_elements = driver.find_elements(By.CLASS_NAME, 'of-price-saleprice')

# Extract text for name and price
for name_element, price_element in zip(name_elements, price_elements):
    name = name_element.text.strip()
    price = price_element.text.strip()
    ws.append([name, price])

# Save the Excel file
wb.save('Movistar_chille//movistar_chile_renewal.xlsx')

# Close the webdriver
driver.quit()
