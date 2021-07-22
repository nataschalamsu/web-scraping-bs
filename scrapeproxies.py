import requests
from bs4 import BeautifulSoup
import concurrent.futures

def getProxies():
  r = requests.get('https://free-proxy-list.net/')
  soup = BeautifulSoup(r.content, 'html.parser')
  table = soup.find('tbody')
  proxies = []
  for row in table:
    if row.find_all('td')[4].text == 'elite proxy':
      print('finding...')
      proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
      print(proxy)
      proxies.append(proxy)
    else:
      pass
  return proxies

def extract(proxy):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
  try:
    r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=1)
    print(r.json(), r.status_code)
  except:
    print('pass')
    pass
  return proxy

proxylist = getProxies()

with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(extract, proxylist)

