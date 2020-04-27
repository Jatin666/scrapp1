import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv
page = requests.get("https://www.skysports.com/premier-league-table")
soups = soup(page.text,'html.parser')
table=[]
points=[]
league_table= soups.find('table', class_='standing-table__table')
for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find(class_='standing-table__cell standing-table__cell--name')
        pl_points= row.find_all('td',class_="standing-table__cell")[9]
        #print(pl_points.text)
        points.append(pl_points.text)
        table.append(pl_team.text.strip())
    #print(table)
    df1= pd.DataFrame(table,points)
    print (df1)