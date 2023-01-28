import requests as re, openpyxl as excel
from bs4 import BeautifulSoup
url='https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone%7CMobiles&requestId=0b077aaa-b734-4650-9883-f95bc193702f&as-backfill=on'
url2="https://www.flipkart.com/search?q=sunflower+oil&sid=eat&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_sc_na_na&as-pos=1&as-type=RECENT&suggestionId=refined+sunflower+oil%7CFood+Products&requestId=d599bf54-5c09-4843-9584-5a4154538236&as-backfill=on&page=1"
response=re.get(url2)
wkbk=excel.Workbook()
page=wkbk.active
page.title='Oil'
page.append(['Product_Name','mrp','link'])
frag=BeautifulSoup(response.text,'html.parser')
img=frag.find_all('img',class_="_396cs4")
data=frag.find('div',class_='_36fx1h _6t1WkM _3HqJxg')
'''for i in img:
    page.append([i.attrs["src"].strip()])
'''
collections=[]
product_names=[]
data=data.find('div',class_="_1YokD2 _3Mn1Gg").find_all('div', class_="_1AtVbE col-12-12")
for i in range(len(data)):
  name=data[i].find_all('div', class_="_4ddWXP")
  for i in name:
    collections.append(i)
    product_names.append(i.text)
for product in product_names:
  print(product)
    #print(len(oil_name))
#for i in range(len(data)):
  # print([data[i].find('a',class_='s1Q9rs').text,data[i].find('div',class_='_30jeq3').text.split("₹")[1],img[i].attrs["src"].strip()])
    #print('done developer')
    # #wkbk.save('filpkart_data_01-26-2023.xlsx')