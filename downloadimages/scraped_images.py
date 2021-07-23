import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.airbnb.com/s/Manado--Sulawesi-Utara/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&place_id=ChIJXebM__mehzIR764dCXoiNwQ&query=Manado%2C%20Sulawesi%20Utara&checkin=2021-07-26&checkout=2021-07-27&adults=1&source=search_blocks_selector_p1_flow&search_type=search_query'


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

def imagedown(url, folder):
  try:
    print('create folder...')
    os.mkdir(os.path.join(os.getcwd(), folder))
  except:
    pass
  os.chdir(os.path.join(os.getcwd(), folder))
  r = requests.get(url, headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')

  images = soup.find_all('img')

  for image in images:
    print(image['src'])
    link = image['src']
    name = link.replace('https://a0.muscache.com/im/pictures/', '').replace('.jpg?im_w=720', '')
    with open(name + '.jpg', 'wb') as f:
      img = requests.get(link)
      f.write(img.content)
      print('writing: ', name)

imagedown('https://www.airbnb.com/s/Bandung--Jawa-Barat--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&place_id=ChIJsdcXjLjuaC4R4Lgo_PHoAQM&query=Bandung%2C%20Jawa%20Barat%2C%20Indonesia&checkin=2021-07-26&checkout=2021-07-27&adults=1&source=search_blocks_selector_p1_flow&search_type=search_query', 'bandung')
