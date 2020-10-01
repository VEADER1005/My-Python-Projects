from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import smtplib
import time

my_url = "https://www.croma.com/acer-predator-helios-300-ph315-52-un-q54si-005-core-i7-9th-gen-windows-10-gaming-laptop-16-gb-ram-1-tb-hdd-+-256-gb-ssd-nvidia-geforce-rtx-2060-+-6-gb-graphics-39-62cm-black-/p/223239"
def check_price():
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers= page_soup.findAll("div",{"class":"product-details-price"})
    container = containers[0]

#price_croma
    price_container = container.findAll("span",{"class":"pdpPrice"})
    price = price_container[0].text
    price_c=''.join(price.split(','))
    price_croma=''.join(price_c.split('₹'))
    price_croma = price_croma[0:6]
    print(price_croma)

#send_Mail
    if int(price_croma) >  100000:
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sj.sahiljain1005@gmail.com','gozptqbkgomxdfho')

    subject='The price fell down in Croma!!'
    body = " the price of Helios 300 has fallen click the link below to see:https://www.croma.com/acer-predator-helios-300-ph315-52-un-q54si-005-core-i7-9th-gen-windows-10-gaming-laptop-16-gb-ram-1-tb-hdd-+-256-gb-ssd-nvidia-geforce-rtx-2060-+-6-gb-graphics-39-62cm-black-/p/223239 "
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        "sj.sahiljain1005@gmial.com",
        'sj.sahiljain1005@gmail.com',
        msg
        )
    print("HEY the email has been sent")
    server.quit()


while(True):
    check_price()
    time.sleep(86400)

