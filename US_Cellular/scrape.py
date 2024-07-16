import requests


url = "https://www.uscellular.com/rp-server/commerce/v1/mobileDeviceOfferingX9?salesChannel=WR&isSMB=false&sort=popularity&filters=category.id%3D%3D11476938_11477008&bundledInMobileOffering=&qualificationCriteria=&orderFlow=NewLine&customerTypeSubtype=R_REG&zipcode=95461&selectedPriceType=EIP"
response = requests.get(url)
data = response.json()

list_of_device_id = []
items = data['items']
for i in range(len(items)):
    list_of_device_id.append(items[i]['id'])


base_url = "https://www.uscellular.com/rp-server/commerce/v1/mobileDeviceOffering/{}?salesChannel=WR&embed=productSpecification&levelOfData=variantGroupOffering%2CpriceOptionItem%2CstockAvailability%2CpriceOptionItemWithoutCondition&isSMB=false&orderFlow=NewLine&customerTypeSubtype=R_REG&zipcode=95461"
new_urls = [base_url.format(item) for item in list_of_device_id]

for url in new_urls:

    response = requests.get(url)
    data = response.json()

    # print(data['calculateVariantGroupInformation']['displayName'])
    # print(data['calculateVariantGroupInformation']['variantGroupCharacteristic'][1]['value'])
    l = data['calculateVariantGroupInformation']['variantGroupCharacteristic'][1]['value']
    memory = set([item['value'] for item in l])
    memory = list(memory)
    memory.sort()
    print(memory)

    prices = []
    for i in range(len(data['calculateVariantGroupInformation']['variantItem'])):
        # print(data['calculateVariantGroupInformation']['variantItem'][i]['msrp'])
        prices.append(data['calculateVariantGroupInformation']['variantItem'][i]['msrp'])
        
    m = set(prices)
    prices = list(m)
    prices = [float(x) for x in prices]
    prices.sort()

    device_memory_to_price_mapped = {}
    for i, size in enumerate(memory):
        device_memory_to_price_mapped[size] = prices[i]
