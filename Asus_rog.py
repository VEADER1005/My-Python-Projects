from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
URL = "https://www.amazon.in/G512LV-AZ060T-i7-10750H-RTX2060-6GB-FHD-240hz-Backlit-4/dp/B08HM7JSHM/ref=sr_1_11?dchild=1&keywords=asus+rog&qid=1599717194&sr=8-11"
uClient=ureq(URL)
page_html=uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser")


containers= page_soup.findAll("div",{"id":"desktop_unifiedPrice"})
container=containers[0]
price_container= container.findAll("span",{"class":"a-size-medium a-color-price priceBlockBuyingPriceString"})


price = price_container[0].text.strip()
converted_prices = ''.join(price.split(","))
converted_price =''.join(converted_prices.split('₹'))

print(converted_price)






