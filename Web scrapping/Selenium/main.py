from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service('C:/Users/Vivek Sharma/Documents/pythonProject/Chrome_driver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

events_time = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
events_name = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')

event = {}

for n in range(len(events_name)):
    event[n] = {"Time": events_time[n].text, "Name": events_name[n].text}

print(event)
