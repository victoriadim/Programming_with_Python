import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population')
soup = bs(r.content, features="lxml")

data = {}
table = soup.find('table', attrs={'class':'sortable wikitable sticky-header col2left col7left'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows[2:5]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data[cols[1]] = {
        'country_population': int(cols[4].replace(',', '')),
        'country_population_percentage': float(cols[3].replace('%', ''))
    }

print(data)