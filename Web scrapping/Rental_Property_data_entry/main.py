import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_path = 'C:/Users/Vivek Sharma/Documents/pythonProject/Chrome_driver/chromedriver.exe'
URL = "https://housing.com/rent/search-P1fboq6zsqo735tsoU7z6"
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdcj3tt4LDhN0bAE9TUy4tLclItWn9oBCb5sOyAQnm1u7ceQQ/viewform?usp=sf_link"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,",
    "Accept-Language": "en-US,en;q=0.9",
           }

response = requests.get(url=URL, headers=headers)
content = response.text
soup = BeautifulSoup(content, 'html.parser')

property_name = []
address_list = []
price_list = []
links_list = []

address = soup.findAll(name="div", class_="new-title css-11nfaq3")
for a in address:
    property_name.append(a.text.split('for rent in')[0])
    address_list.append(a.text.split('for rent in')[1])

print(property_name, len(property_name))
print(address_list, len(address_list))

prices = soup.findAll(name="div", class_="css-2fyglz")
for p in prices:
    price_list.append(p.text)

print(price_list)
print(len(price_list))

links = soup.findAll(name="a", class_="css-vhnx41", href=True)
for link in links:
    full_link = "https://housing.com"+link["href"]
    links_list.append(full_link)

print(links_list, len(links_list))

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url=google_form_url)
driver.maximize_window()
time.sleep(3)

i = 0
while i < len(property_name):

    property_name_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

    property_name_input.send_keys(property_name[i])
    time.sleep(1)
    address_input.send_keys(address_list[i])
    time.sleep(1)
    price_input.send_keys(price_list[i])
    time.sleep(1)
    link_input.send_keys(links_list[i])

    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(3)

    next_submission = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_submission.click()
    time.sleep(2)

    i += 1

driver.quit()

