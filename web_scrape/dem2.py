import requests as request
from bs4 import BeautifulSoup
url="https://www.google.com/search?q=zoominfo+Javista"
response=request.get(url)
frag=BeautifulSoup(response.text,'html.parser')
print(frag.find('div',class_="main"))