import requests

url = "https://www.uscellular.com/rp-server/commerce/v1/mobileDeviceOfferingX9?salesChannel=WR&isSMB=false&sort=popularity&filters=category.id%3D%3D11476938_11477008&bundledInMobileOffering=&qualificationCriteria=&orderFlow=NewLine&customerTypeSubtype=R_REG&zipcode=95461&selectedPriceType=EIP"
response = requests.get(url)
data = response.json()

l = []
items = data['items']
for i in range(len(items)):
    l.append(items[i]['id'])
print(len(l))