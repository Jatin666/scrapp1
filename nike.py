import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv
page = requests.get("https://www.nike.com/in/w/mens-shoes-nik1zy7ok")
soups = soup(page.content,'html.parser')
dict1={

}
dict2={

}

items =soups.find_all(class_="product-card__link-overlay")
items2=soups.find_all(class_="product-card__price")
for div in items:
    dict1['name of the shoes'] = div.text
    print(dict1)
for div in items2:
    dict2['price'] = div.text
    print(dict2)
