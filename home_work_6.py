import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
count_response = len(response.history)
last_response = response

print(f"Количество редиректов: {count_response}")
print(f"Итоговый URL: {last_response.url}")