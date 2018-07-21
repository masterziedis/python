import requests
url = "http://www.google.com"
res = requests.get(url)

print(f"your request to {url} was {res.status_code}")