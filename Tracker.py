import requests
from bs4 import BeautifulSoup

#Enter the URL of the desired product.
URL = 'https://www.amazon.de/-/en/Sony-Frame-Interchangeable-Camera-SEL2870/dp/B00Q2KEVA2/ref=sr_1_1?crid=3JZD7HLYKMDLV&keywords=sony+a7&qid=1655221154&sprefix=sony+a%2Caps%2C158&sr=8-1'

#Enter Agent. Google search: My user agent.
agent = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'}

#Requests the page
page = requests.get(URL, headers=agent)

#Calls BeautifulSoup and parsers the HTML page.
soup = BeautifulSoup(page.content, 'html.parser')

#Extracts the product name and the price.
product = soup.find(id="productTitle").get_text()
price = soup.find('span', {'class' : 'a-price-whole'}).get_text()

#Converts the price to a float and changes "," to "."
disallowed_characters = ","
for character in disallowed_characters:
      price = price.replace(character, ".")
converted_price = float(price[0:5])

#Price Condition to send an email.



print(converted_price)
print(product)
