import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nba.com/stats'
filename = 'NBA_stats.csv'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

player_data = soup.find_all('tr', class_='LeaderBoardPlayerCard_lbpcTableRow___Lod5')
players = [player_data[i].a.text for i in range(45)]

field_data = soup.find_all('h2', class_='LeaderBoardCard_lbcTitle___WI9J')
fields = [field_data[i].text for i in range(9)]

data = [['Field', 'Rank', 'Player']]
for i in range(45):
    data.append([fields[i//5], i%5+1,players[i]])

with open(filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
