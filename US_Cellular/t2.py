import requests
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.uscellular.com/rp-server/commerce/v1/mobileDeviceOfferingX9?salesChannel=WR&isSMB=false&sort=popularity&filters=category.id%3D%3D11476938_11477008&bundledInMobileOffering=&qualificationCriteria=&orderFlow=NewLine&customerTypeSubtype=R_REG&zipcode=95461&selectedPriceType=EIP"
response = requests.get(url)
data = response.json()

list_of_device_id = []
items = data['items']
for i in range(len(items)):
    list_of_device_id.append(items[i]['id'])

base_url = "https://www.uscellular.com/rp-server/commerce/v1/mobileDeviceOffering/{}?salesChannel=WR&embed=productSpecification&levelOfData=variantGroupOffering%2CpriceOptionItem%2CstockAvailability%2CpriceOptionItemWithoutCondition&isSMB=false&orderFlow=NewLine&customerTypeSubtype=R_REG&zipcode=95461"
new_urls = [base_url.format(item) for item in list_of_device_id]

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Name", "Price"])

# Selenium setup
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait for elements to appear

for idx, url in enumerate(new_urls):
    try:
        response = requests.get(url)
        data = response.json()

        name = data['calculateVariantGroupInformation']['displayName']

        l = data['calculateVariantGroupInformation']['variantGroupCharacteristic'][1]['value']
        memory = set([item['value'] for item in l])
        memory = list(memory)
        memory.sort()

        prices = []
        for i in range(len(data['calculateVariantGroupInformation']['variantItem'])):
            prices.append(data['calculateVariantGroupInformation']['variantItem'][i]['msrp'])

        m = set(prices)
        prices = list(m)
        prices = [float(x) for x in prices]
        prices.sort()

        device_memory_to_price_mapped = {}
        for i, size in enumerate(memory):
            device_memory_to_price_mapped[size] = prices[i]

        for size, price in device_memory_to_price_mapped.items():
            ws.append([f"{name} {size}", price])

    except Exception as e:
        print(f"Error processing URL: {url}")
        print(f"Error message: {e}")
        # driver.get(url)  # Open the URL with Selenium

        # # Collect memory and price using Selenium
        # memory_elements = driver.find_elements(By.ID, f"labelfor_memory_{idx}")
        # price_elements = driver.find_elements(By.CLASS_NAME, "price-amount")

        # for i in range(len(memory_elements)):
        #     memory = memory_elements[i].text
        #     price = price_elements[i].text
        #     ws.append([f"{name} {memory}", price])

wb.save("us_cellular1.xlsx")

driver.quit()  # Close the Selenium WebDriver
