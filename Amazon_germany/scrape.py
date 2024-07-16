from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your webdriver executable
url = 'https://www.amazon.de/s?k=samsung+smartphone&rh=n%3A562066%2Cp_89%3ASamsung&dc&language=en&ds=v1%3ArXX78TyPXGGrJjGxvYDFiPzNRFfX0JUeDKVIUF7%2BIUE&rnid=669059031&ref=sr_nr_p_89_1'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

# Find elements for name and price
name_elements = driver.find_elements(By.CLASS_NAME, 'a-size-medium.a-color-base.a-text-normal')
price_elements = driver.find_elements(By.CLASS_NAME, 'a-price')

# Extract text for name and price
for name_element, price_element in zip(name_elements, price_elements):
    name = name_element.text.strip()
    price = price_element.text.strip()
    print(f"Name: {name}, Price: {price}")

# Close the webdriver
driver.quit()
