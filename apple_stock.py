from bs4 import BeautifulSoup
import requests

with open('Apple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


table = soup.find("tbody")
rows = table.find_all("tr")


for row in rows[0:21]:
  cell = row.find_all("td")
  date = cell[0].text.split()
  stock_price = cell[5].text.split()
  apple_history = f"Date: {date}" + ", " + f"Price: {stock_price}"
  print(apple_history)