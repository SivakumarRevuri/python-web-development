import requests
import json

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/"

# response = requests.get(endpoint)
# print(response.text) # returns a string response
# a normal, HTTP REQUEST ==> HTML
# and, REST API HTTP REQUEST ==> JSON
endpoint = "https://httpbin.org/anything"
# response = requests.get(endpoint)
# print(response.json())
# with open('json-format.json', 'w') as file:
#     print(json.dump(response.text, file ,indent=2)) # retuns in JSON format.


# response = requests.get(endpoint, json={"query": "HelloWorld!!!"}) # passing input parameter
# response = requests.get(endpoint, data={"query": "HelloWorld!!!"}) # passing in diff param

# print(response.status_code) # returns you a StatusCode

endpoint = 'http://localhost:8000/api'
response = requests.get(endpoint)

print('LocalHost: ', response.status_code)
print(response.json())
