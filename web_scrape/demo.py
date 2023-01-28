from bs4 import BeautifulSoup
import requests as re, openpyxl as ex

file=ex.Workbook()
print(file.sheetnames)
page=file.active
page.title='Top rated movies'
print(file.sheetnames)
page.append(['id','name','year','rating'])
url='https://www.imdb.com/india/top-rated-tamil-movies/'
response=re.get(url)
try:
    soup=BeautifulSoup(response.text,'html.parser')
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        id=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')  
        name=movie.find('td',class_="titleColumn").find('a').text
        year=movie.find('span',class_="secondaryInfo").text
        rating=movie.find('td',class_="ratingColumn").find('strong').attrs['title']
        print(f'{id[0]}:{name} {year} {rating}')
        page.append([id[0],name,year,rating])
except Exception as e:
    print(e)
file.save('scrapedata.xlsx')
