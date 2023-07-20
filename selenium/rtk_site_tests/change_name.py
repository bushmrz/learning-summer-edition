from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from login import driver

url = 'https://b2c.passport.rt.ru/auth'
driver = webdriver.Chrome()
driver.get(url)

for cookie in pickle.load(open('cookies', 'rb')):
    driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()
time.sleep(25)

open_popup_button = driver.find_element(By.CLASS_NAME, 'user-info__edit')


def input_fio(first_name=" ", last_name=" ", surname=" "):

    open_popup_button.click()
    time.sleep(10)

    edit_firstname = driver.find_element(By.ID, 'user_firstname')
    edit_lastname = driver.find_element(By.ID, 'user_lastname')
    edit_surname = driver.find_element(By.ID, 'user_patronymic')

    edit_firstname.clear()

    edit_firstname.send_keys(Keys.CONTROL + 'a')
    edit_firstname.send_keys(first_name)
    time.sleep(5)

    edit_lastname.clear()

    edit_lastname.send_keys(Keys.CONTROL + 'a')
    edit_lastname.send_keys(last_name)
    time.sleep(5)

    edit_surname.send_keys(Keys.CONTROL + 'a')
    edit_surname.send_keys(surname)
    time.sleep(5)

    save_button = driver.find_element(By.ID, 'user_contacts_editor_save')


    save_button.click()
    time.sleep(15)


input_fio('Алиса', "Фамилия-Фамилия", "Павловна")
input_fio('Ия', 'Шнайдер')
