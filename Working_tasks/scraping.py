import requests
import pandas as pd
from os.path import exists
import os
from bs4 import BeautifulSoup as bs

r = requests.get('https://bnb.bg/Statistics/StInterbankForexMarket/index.htm')
soup = bs(r.content, features="lxml")

data = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')
columns=["Код на валута","нещо","СП-Купува","СП-Продава","Купени-процент","Продадени-процент","Обем купени","Обем продадени","КП-Купува","КП-Продава"]
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
df = pd.DataFrame(data,
columns=columns)


def clean_space(value):
    return value.replace(" ", "") if value else value


df['Обем продадени'] = df['Обем продадени'].apply(clean_space)
df['Обем продадени'] = df['Обем продадени'].astype(float)
df = df.sort_values(by='Обем продадени', ascending=False)
directory = os.getcwd()
file_exists = exists(os.path.join(directory, 'exchange_rates.csv'))
if file_exists:
    old_df = pd.read_csv('exchange_rates.csv')
    if not df.equals(old_df):
        df.to_csv('exchange_rates.csv', index=False, encoding='utf-8-sig')
else:
    df.to_csv('exchange_rates.csv', index=False, encoding='utf-8-sig')

print(df)