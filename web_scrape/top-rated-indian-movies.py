from bs4 import BeautifulSoup
import requests as re, openpyxl as ex

file=ex.Workbook()
page=file.active
page.title='Top rated movies'
page.append(['id','name','year','rating'])
url='https://www.imdb.com/india/top-rated-indian-movies/'
response=re.get(url)
try:
    soup=BeautifulSoup(response.text,'html.parser')
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        id=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')  
        name=movie.find('td',class_="titleColumn").find('a').text
        year=movie.find('span',class_="secondaryInfo").text
        rating=movie.find('td',class_="ratingColumn").find('strong').attrs['title']
        page.append([id[0],name,year,rating])
    file.save('top_rated_indian_movies.xlsx')
except Exception as e:
    print(e)
