import grequests
from bs4 import BeautifulSoup
import pandas as pd

def get_urls():
  urls = []
  for x in range(1, 11):
    urls.append(f'https://www.canoeandkayakstore.co.uk/collections/activity-recreational-beginner?page={x}')
  return urls

def get_data(urls):
  reqs = [grequests.get(link) for link in urls]
  res = grequests.map(reqs)
  return res

def parse(res):
  productlist = []
  for r in res:
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('div', {'class': 'product-grid-item__info'})
    for item in items:
      product = {
        'title': item.find_all('a')[0].text.strip(),
        'price': item.find('span', {'class': 'product-grid-item-price'}).find_all('span')[0].text.strip(),
        'availablity': item.find('span', {'class': 'product-grid-item__info__availability--value'}).text.strip()
      }
      productlist.append(product)
      print('Added: ', product)
    return productlist

urls = get_urls()
response = get_data(urls)
df = pd.DataFrame(parse(response))
df.to_csv('canoes.csv', index=False)

