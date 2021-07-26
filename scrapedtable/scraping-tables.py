import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.skysports.com/premier-league-table/2020'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_= 'standing-table__table')

def parse():
  pl_team_list = []
  for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
      pl_team = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
      pl_points = row.find_all('td', class_ = 'standing-table__cell')[9].text.strip()

      teams_pts = {
        'team': pl_team,
        'pts': pl_points
      }

      pl_team_list.append(teams_pts)
    return pl_team_list

df = pd.DataFrame(parse())
df.to_csv('pl_team_list.csv', index=False)
    