from bs4 import BeautifulSoup
import requests

# URL of page
url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

for row in table.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        cell1_data = cells[0].get_text()
        cell2_data = cells[1].get_text()
        print('Cell 1:', cell1_data)
        print('Cell 2:', cell2_data)
