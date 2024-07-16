from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl


url = 'https://www.uscellular.com/devicelist'
driver = webdriver.Chrome()
driver.get(url)

# time.sleep(30)

reject_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-reject-all-handler"]')))
reject_button.click()

# Wait for the zip code input to be visible and enter a zip code
zip_code_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'zip-code')))
zip_code_input.send_keys('95461')

# Click the continue button
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dialog"]/div[1]/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/button')))
continue_button.click()
time.sleep(15)
# Find all 'a' tags with the specified class
a_tags = driver.find_elements(By.CLASS_NAME, 'link.without-div.font-16.animated-link.m-t-16.display-flex.justify-content-end.align-items-center.buy-now-link')

# Extract href values and store them in a list
href_values = [a.get_attribute('href') for a in a_tags]




# Start a new Chrome session
driver = webdriver.Chrome()

n = 0
for url in href_values:
    driver.get(url)
    
    if n == 0:
        reject_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-reject-all-handler"]')))
        reject_button.click()

        # Wait for the zip code input to be visible and enter a zip code
        zip_code_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'zip-code')))
        zip_code_input.send_keys('95461')

        # Click the continue button
        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dialog"]/div[1]/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/button')))
        continue_button.click()
    n += 1
    # Wait for the page to load
    time.sleep(2)

    # Initialize index
    index = 0

    # Load the existing Excel file or create a new one if it doesn't exist
    try:
        wb = openpyxl.load_workbook('us_cellular.xlsx')
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        wb.active.append(['Name', 'Price'])
        wb.save('us_cellular.xlsx')

    ws = wb.active

    while True:
        try:
            memory_path = '//*[@id="memory_' + str(index) + '"]'
            memory_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, memory_path)))
            if len(memory_buttons) == 0:
                # If there are no memory buttons, directly extract the name and price
                price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="labelfor_FULL_PRICE"]/div[2]/span')))
                name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/div/h1/span').text
            else:
                for button in memory_buttons:
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", button)
                price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="labelfor_FULL_PRICE"]/div[2]/span')))
                
                # Extract the name
                name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/div/h1/span').text
        
            # Extract the price information
            price_text = price.text
            # Append the name and price to the Excel sheet
            ws.append([name, price_text])
            wb.save('us_cellular.xlsx')
            
            # Print the name and price for the current memory variant
            print(f'Name: {name}, Price: {price_text}')
            index += 1
        except Exception as e:
            # Print the exception and break the loop
            print(f'Exception: {e}')
            break

# Close the browser session
driver.quit()
