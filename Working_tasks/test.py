import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://bg.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D1%8A%D0%BA_%D0%BD%D0%B0_%D0%B0%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%82%D0%B5_%D0%B4%D1%8A%D1%80%D0%B6%D0%B0%D0%B2%D0%B8_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%B8_%D1%82%D0%B5%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B8')
soup = bs(r.content, features="lxml")

data = {}
table = soup.find('table', attrs={'class': 'wikitable sortable'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows[1:4]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data[cols[0]] = {
        'Столица': str(cols[2]),
        'Езици': str(cols[4])
    }

print(data)