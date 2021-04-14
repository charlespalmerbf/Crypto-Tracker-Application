import requests

from bs4 import BeautifulSoup

import smtplib

import time

URL = 'https://www.coindesk.com/price/xrp'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("div", class_="price-large").get_text()

    converted_price = float(price[1:5])

    if(converted_price > 2.000):

        send_mail()

    print(converted_price)


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login('flymototo@gmail.com', 'ficivtxrrylfyxqw')

    subject = 'XRP Is Above 2$!'

    body = 'Check Your Tokens!'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'flymototo@gmail.com',
        'charliehp@btconnect.com',
        msg
    )

    print('Email Has Been Sent!')

    server.quit()


while(True):

    check_price()

    time.sleep(2400)
