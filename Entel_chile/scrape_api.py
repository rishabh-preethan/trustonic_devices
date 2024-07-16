import requests
import pandas as pd

url = "https://miportal.entel.cl/catalogo/celulares?No=1&Nrpp=170&contentPath=%2Fpages%2Fstorechilepp%2Fcatalogo%2Fcelulares&eIdx=8&sIdx=1&subPath=main%5B1%5D&format=json-rest&_=1711642765580"

response = requests.get(url)
data = response.json()

# Extract name and price from the JSON response
records = data['response']['records']
names = [record['attributes']['displayName'] for record in records]
prices = [record['attributes']['price.formatted'] for record in records]

# Create a DataFrame
df = pd.DataFrame({"Name": names, "Price": prices})

# Save the DataFrame to an Excel file
df.to_excel("Entel_chile//entel_cellphones_api.xlsx", index=False)
