#script to scrape data of laptop from a flipkart website
import requests as re, openpyxl as excel
from bs4 import BeautifulSoup
#url='https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone%7CMobiles&requestId=0b077aaa-b734-4650-9883-f95bc193702f&as-backfill=on'
url2="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=0b2ddddc-0e77-4576-9590-5eaf69bd9b84&as-backfill=on"
response=re.get(url2)
wkbk=excel.Workbook()
page=wkbk.active
soup=BeautifulSoup(response.text,'html.parser')
result=soup.find('div',id="container")
main=result.find('div')
print(main.find('div',_class="_36fx1h _6t1WkM _3HqJxg"))