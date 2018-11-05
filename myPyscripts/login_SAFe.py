#! python3
#log in SAFe

from selenium import webdriver
import time

# use your own account and password
user_name = ''
password = ''

dr = webdriver.Chrome()
dr.get('https://community.scaledagile.com/s/login/')

elems = dr.find_elements_by_css_selector('.inputBox')
elems[0].clear()
elems[0].send_keys(user_name)
elems[1].clear()
elems[1].send_keys(password)


btn = dr.find_element_by_css_selector('.loginButton')
btn.click()
