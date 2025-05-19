import requests

from bs4 import BeautifulSoup

url = "https://www.screener.in/company/WIPPO/consolidated/"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

print(soup.prettify())
