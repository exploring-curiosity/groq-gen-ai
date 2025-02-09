import requests

api_key = '4dhMFQVrFQKE5SRa8RKV4s2y5wUBdDNP0vzFm6Mt'
# url = f'https://api.eia.gov/v2/electricity/rto/region-data/data/?api_key={api_key}&frequency=hourly&data[0]=value&facets[respondent][]=NYISO&start=2025-02-01&end=2025-10-01'
url = f'https://api.eia.gov/v2/electricity/rto/region-sub-ba-data/data/?api_key={api_key}&frequency=hourly&data[0]=value&facets[subba][]=ZONJ&start=2025-02-08T00&end=2025-02-09T00&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'

response = requests.get(url)
data = response.json()

print(data)