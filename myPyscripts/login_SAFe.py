#! python3
#log in SAFe

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get('https://community.scaledagile.com/s/login/')

elems = dr.find_elements_by_css_selector('.inputBox')
elems[0].clear()
elems[0].send_keys('wu.huang@nokia-sbell.com')
elems[1].clear()
elems[1].send_keys('pwd4any!')


btn = dr.find_element_by_css_selector('.loginButton')
btn.click()
