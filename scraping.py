import requests
from bs4 import BeautifulSoup

url = "https://www.instagram.com/?next=%2F"

response = requests.get(url)
print(response.text)