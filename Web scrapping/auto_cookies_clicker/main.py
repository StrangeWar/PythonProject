from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


service = Service('C:/Users/Vivek Sharma/Documents/pythonProject/Chrome_driver/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookies = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')
items_id = [item.get_attribute('id') for item in items]

timeout = time.time() + 10
five_min = time.time() + 60*5


while True:
    cookies.click()

    # Every 5 seconds:
    if timeout < time.time():

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value='#store b')
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookies_upgrades = {}
        for n in range(len(item_prices)):
            cookies_upgrades[item_prices[n]] = items_id[n]

        # Get current cookie count
        money = driver.find_element(by=By.ID, value='money').text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookies_upgrades.items():
            if cost < cookie_count:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 10

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_cps = driver.find_element(by=By.ID, value='cps')
            print(cookie_cps.text)
            break

driver.quit()






