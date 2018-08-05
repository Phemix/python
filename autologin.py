
from selenium import webdriver
from getpass import getpass
import time

usr = input('Enter your username or email: ') 
pwd = getpass('Enter your password: ')

driver = webdriver.Chrome('//usr/local/bin/chromedriver')
driver.get('https://www.facebook.com/')
time.sleep(5)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_w')
login_btn.submit()

