import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "vivekrockss111@gmail.com"
PASSWORD = "hnddatolzulkfcpz"
URL = "https://www.flipkart.com/askprints-a5-sketch-book-50-sheets-set-2-5-8-x-8-3-inch-top-spiral-" \
      "bound-sketchpad-artists-sketching-drawing-acid-free-paper-doodling-pad/p/itm26b45eb76a053?pid=" \
      "SPDFUZ25FDEJQFRK&lid=LSTSPDFUZ25FDEJQFRKJ1DBMQ&marketplace=FLIPKART&q=askprints+sketch+book&store=" \
      "dgv%2Fj6t%2Fsk7&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&otracker1=" \
      "AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&fm=search-autosuggest&iid=d78dd45f-cec7-45bb-b5ee-6240efef36e7." \
      "SPDFUZ25FDEJQFRK.SEARCH&ppt=sp&ppn=sp&ssid=qtl5koifn40000001654962394536&qH=3e878003f7d2bc44"

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=Headers)
content = response.text

soup = BeautifulSoup(content, "lxml")

price = soup.find(name="div", class_="_30jeq3 _16Jk6d").getText()
new_price = int(price[1:])
print(new_price)

product = soup.find(name="span", class_="B_NuCI").getText()
product_name= product.split("|")
print(product_name[0])

if new_price < 300:

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"subject:Price Drop!\n\n{product_name[0]}\nRs {new_price}\nUrl = {URL}",

                            )

    