#! python3
# try to log in qq mail

from selenium import webdriver
import time

# use your own account and password
user_name = ''
password = ''

dr = webdriver.Chrome()
dr.get('http://mail.qq.com')
dr.switch_to.frame('login_frame')
userElem = dr.find_element_by_id('u')
userElem.send_keys(user_name)
pwdElem = dr.find_element_by_id('p')
pwdElem.send_keys(password)
btnElem = dr.find_element_by_id('login_button')
btnElem.click()

time.sleep(20)

"""
try:
    captcha = dr.find_element_by_id('newVcodeArea')
except NoSuchElementException:
    print('no verification')
    
if captcha != None:
    print('verification...operate on the page')
    cur_url = dr.current_url
    while True:
        url_must_changed = dr.current_url
        if url_must_changed != cur_url:
            break
        time.sleep(1)
"""        

    
