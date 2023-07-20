from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pickle

from data import login, password


url = 'https://b2c.passport.rt.ru/auth'
driver = webdriver.Chrome()


def auth():

    driver.get(url)
    time.sleep(15)
    login_input = driver.find_element(By.ID, 'username')
    login_input.clear()
    login_input.send_keys(login)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(7)

    login_button = driver.find_element(By.ID, 'kc-login')
    login_button.click()
    time.sleep(10)

    pickle.dump(driver.get_cookies(), open('cookies', 'wb'))


auth()
