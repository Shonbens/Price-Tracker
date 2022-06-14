import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/-/en/Sony-Frame-Interchangeable-Camera-SEL2870/dp/B00Q2KEVA2/ref=sr_1_1?crid=3JZD7HLYKMDLV&keywords=sony+a7&qid=1655221154&sprefix=sony+a%2Caps%2C158&sr=8-1'

agent = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'}

page = requests.get(URL, headers=agent)

soup = BeautifulSoup(page.content, 'html.parser')

product = soup.find(id="productTitle").get_text()

print(product)

price = soup.find(id='priceblock_ourprice').get_text()