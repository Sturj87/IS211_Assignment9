from bs4 import BeautifulSoup
import requests

# URL of page
url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/'

response = requests.get(url)
#print(response)

page_html = response.content

soup = BeautifulSoup(page_html, "html.parser")
table = soup.find("tbody")
rows = table.find_all("tr")



for row in rows[0:21]:
  cell = row.find_all("td")
  results = cell[0].text.split()
  touchdown_passes = cell[8].text.split()
  results_2 = f"His touchdown passes stats is: {touchdown_passes}"
  first_name = results[4]
  last_name = results[5]
  full_name = first_name + "," + last_name
  player_position = results[6]
  plater_team = results[7]
  top_20 = f"Player name: {full_name}" + ". " + f"Position: {player_position}" + ", " + f"Team: {plater_team}."
  print(top_20, results_2)