import requests

from bs4 import BeautifulSoup

url = "https://www.google.com" # Replace with the actual URl

response = requests.get(url)

# Parse HTMl
soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify())
#print(soup.find("a").text)

#print(soup.findAll("a"))

#divs = soup.find_all("div",class_ = "my-class")
element = soup.find(id = "unique-id")