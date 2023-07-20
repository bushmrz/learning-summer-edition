from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/?hl=RU")
time.sleep(5)

element = driver.find_element(By.ID, "APjFqb")
element.send_keys("Mr Kitty")
element.send_keys(Keys.ENTER)
time.sleep(15)
