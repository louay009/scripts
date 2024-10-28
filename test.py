import requests

proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080',
}

url = 'http://example.com'

response = requests.get(url, proxies=proxy)

print(response.status_code)
print(response.text)