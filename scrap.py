import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv
page = requests.get("https://www.home24.de/kategorie/wohnzimmermoebel/sofas-und-couches/?campaign=party&hidecms=true")
soups = soup(page.content,'html.parser')
name=[]
price=[]
items = soups.find_all(class_="article-tile__wrap")
#print(items[0])
items2=( soups.find_all(class_='article-tile__name'))
for div in items2:
    #print (div.text)
    name.append((div).text)
#print(name)
items3=(soups.find_all(class_="article__price"))
for span in items3:
    price.append((span.text))
#print(price)
df1= pd.DataFrame(name,price)
print(df1)
df1.to_csv('scrapping.csv')
