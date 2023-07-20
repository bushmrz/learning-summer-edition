from selenium import webdriver
import time
from fake_useragent import UserAgent as UA
from selenium.webdriver.chrome.options import Options

# create new UserAgent object
user = UA()

# options
options = Options()

# change useragent
options.add_argument(f'--user-agent={user.random}')

driver = webdriver.Chrome(options=options)

driver.get('https://whatmyuseragent.com/')
time.sleep(15)



