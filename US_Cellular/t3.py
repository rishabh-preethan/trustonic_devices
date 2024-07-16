from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://www.uscellular.com/devicelist'
driver = webdriver.Chrome()
driver.get(url)

# time.sleep(30)
zip_code_input = driver.find_element(By.ID,'zip-code')
zip_code_input.send_keys('95461')

# Click continue button
continue_button = driver.find_element(By.CSS_SELECTOR,'.serviceability-buy-flow-button-continue.disabled.btn')
continue_button.click()
time.sleep(15)
# Find all 'a' tags with the specified class
a_tags = driver.find_elements(By.CLASS_NAME, 'link.without-div.font-16.animated-link.m-t-16.display-flex.justify-content-end.align-items-center.buy-now-link')

# Extract href values and store them in a list
href_values = [a.get_attribute('href') for a in a_tags]

print(href_values)
print(len(href_values))

# for url in href_values:
    
    
