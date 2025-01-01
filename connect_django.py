import requests
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='cities_json/'
response=requests.get(BASE_URL+ENDPOINT)
print(response.json())
print(type(response.json()))
data=response.json()
print('Data from django app:')
print('*'*50)
print('City ID:',data['id'])
print('City Name:',data['city_name'])
print('State Name:',data['state_name'])
