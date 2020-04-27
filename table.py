import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv

from pandas import DataFrame

page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
soups = soup(page.text,'html.parser')
table1=[]
points=[]
leauge_table= soups.find_all('table',class_="table")
#print(leauge_table)
#a=soups.find_all('tr',class_="table-body")
#b=soups.find_all('td',class_="table-body__cell rankings-table__team")
for items in soups.find_all('span',class_="u-hide-phablet"):
    table1.append(items.text)
#print(table1)
for item in soups.find_all('td',class_="table-body__cell u-text-right rating"):
    points.append(item.text)
list1 = [table1],[points]
df = pd.DataFrame(list1)
print(df)
df.to_csv('cricket.csv')