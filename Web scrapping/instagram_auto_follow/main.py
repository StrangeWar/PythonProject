import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

INSTA_ID = 'G_E_A_R_5'
PASSWORD = 'Vivek@557'
driver_path = 'D:/pythonProject/Chrome_driver/chromedriver.exe'


class InstaFollower:
    def __init__(self, path):
        service = Service(path)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        login = self.driver.find_element(by=By.NAME, value='username')
        password = self.driver.find_element(by=By.NAME, value='password')

        login.send_keys(INSTA_ID)
        password.send_keys(PASSWORD)
        time.sleep(2)

        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/nasa/")
        time.sleep(5)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='follower').click()
        time.sleep(2)

    def follow(self):
        """For start following a person who is not already followed"""

        while True:
            def sleep_for_period_of_time():
                limit = random.randint(3, 6)
                time.sleep(limit)
            try:
                list_of_people = self.driver.find_elements(by=By.XPATH, value="//div[@class='_aano']//*//*//div/div//button//*//*")
                for person in list_of_people:
                    if person.text == "Follow":
                        person.click()
                        sleep_for_period_of_time()
                self.driver.execute_script("arguments[0].scrollIntoView(true);", list_of_people[-1])

            except IndexError:
                break

            except Exception as e:
                print(e)


bot = InstaFollower(path=driver_path)
bot.login()
bot.find_followers()
bot.follow()

