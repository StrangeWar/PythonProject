from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service('C:/Users/Vivek Sharma/Documents/pythonProject/Chrome_driver/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# statistics_no = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
#
# statistics_no.click()

# portal = driver.find_element(by=By.LINK_TEXT, value='Community portal')
# portal.click()

f_name = driver.find_element(by=By.NAME, value="fName")
f_name.send_keys("vivek")


l_name = driver.find_element(by=By.NAME, value='lName')
l_name.send_keys("sharma")

email = driver.find_element(by=By.NAME, value='email')
email.send_keys("vivek@gmail.com")

submit = driver.find_element(by=By.CSS_SELECTOR, value='form button')
submit.click()



