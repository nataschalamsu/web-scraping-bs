from requests_html import HTMLSession
import pandas as pd

url = 'https://www.beerwulf.com/en-gb/c?page=1&price=Discounted%20Products%0A'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

# print(r.status_code)

products = r.html.xpath('//*[@id="product-items-container"]', first=True)

def parse():
  beerlist = []
  for item in products.absolute_links:
    r = s.get(item)
    div = r.html.find('div.callout', first=True)

    try:
      name = div.xpath('//h1/text()', first=True)
    except:
      name = 'No Name'

    price = r.html.find('span.price', first=True).text

    if r.html.find('div.add-to-cart-container'):
      stock = 'in stock'
    else:
      stock = 'out of stock'

    beer = {
      'name': name,
      'price': price,
      'stock': stock
    }

    beerlist.append(beer)
  return beerlist

df = pd.DataFrame(parse())
df.to_csv('beers.csv', index=False)