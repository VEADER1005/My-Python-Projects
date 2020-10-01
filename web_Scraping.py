from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import smtplib
import time

my_url = " https://www.flipkart.com/acer-predator-helios-300-core-i7-9th-gen-16-gb-1-tb-hdd-256-gb-ssd-windows-10-home-6-graphics-nvidia-geforce-rtx-2060-ph315-52-74dx-gaming-laptop/p/itm887e3873e143c?pid=COMFHNY8NUTBD3C7&lid=LSTCOMFHNY8NUTBD3C7A12RW1&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a2441e08-0dbf-4ee1-92d3-3f28c2f18334.COMFHNY8NUTBD3C7.SEARCH&ppt=sp&ppn=sp&ssid=jp8b7ubyxc0000001599452691217&qH=3901767301d199d8"
def check_price():
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")


    containers=page_soup.findAll("div",{"class":"_3Z5yZS NDB7oB _12iFZG _3PG6Wd"})
    container = containers[0]
#name_flipkart
    name_container = container.findAll("span",{"class":"_35KyD6"})
    name = name_container
    print(name)
#price_Flipkart
    price_container = container.findAll("div",{"class":"_1vC4OE _3qQ9m1"})
    price = price_container[0].text.strip()
    price_f= ''.join(price.split(','))
    price_flipkart =int(''.join(price_f.split("₹")))
    print(price_flipkart)

#send_Mail
    if price_flipkart < 100000:
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sj.sahiljain1005@gmail.com','gozptqbkgomxdfho')

    subject='The price fell down!!'
    body = " the price of Helios 300 has fallen click the link below to see https://www.flipkart.com/acer-predator-helios-300-core-i7-9th-gen-16-gb-1-tb-hdd-256-gb-ssd-windows-10-home-6-graphics-nvidia-geforce-rtx-2060-ph315-52-74dx-gaming-laptop/p/itm887e3873e143c?pid=COMFHNY8NUTBD3C7&lid=LSTCOMFHNY8NUTBD3C7A12RW1&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a2441e08-0dbf-4ee1-92d3-3f28c2f18334.COMFHNY8NUTBD3C7.SEARCH&ppt=sp&ppn=sp&ssid=jp8b7ubyxc0000001599452691217&qH=3901767301d199d8"
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
