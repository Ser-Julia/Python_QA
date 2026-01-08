#from json.decoder import JSONDecodeError
import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#print(response.status_code)
#print(response.text)
first_response = response.history[0]
second_response = response
print(first_response.url)
print(second_response.url)
'''
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not JSON format")
'''