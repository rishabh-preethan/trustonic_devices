from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver
driver = webdriver.Chrome()

# Open the webpage
url = 'https://catalogo.movistar.com.pe/iphone-14'
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

    # Get the memory and price
    memory = memory_button.text
    try:
        device_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'inner'))).text
        price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_price_cash'))).text
    except Exception as e:
        device_name = "N/A"
        price = "N/A"
        print(f"Error getting device name and price: {e}")

    print(f"Memory: {memory}, Device Name: {device_name}, Price: {price}")

# Close the WebDriver
driver.quit()
