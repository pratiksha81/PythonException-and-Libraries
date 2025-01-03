import requests

response = requests.get("https://localhost:7278/api/Authors", verify=False)
print(response.json()) #only works if the api is in running condition 