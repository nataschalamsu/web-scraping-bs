import requests
from bs4 import BeautifulSoup
import time

def get_urls():
  urls = []
  for x in range(1, 51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{x}.html')
  return urls

def parse_data(urls):
  for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find_all('article', {'class': 'product_pod'})
    for item in data:
      name = item.find('h3').text
      price = item.find('p', {'class': 'price_color'})
      print(name, price)
  return

if __name__ == '__main__':
  start = time.perf_counter()
  urls = get_urls()
  parse_data(urls)
  fin = time.perf_counter() - start
  print(fin)

# time taken 38.205088792