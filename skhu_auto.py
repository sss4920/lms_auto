from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'http://lms.skhu.ac.kr/ilos/main/main_form.acl'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('.header_login.login-btn-color').click()
f=open("mytext.txt","r")
id_me = "id 입력하자"
password_me = "pass 입력하자"
loopcount = 1
for line in f.readlines():
    if loopcount ==1:
        id_me = line
        loopcount+=1
    else:
        password_me = line
action.send_keys(id_me).perform()
driver.find_element_by_css_selector('#usr_pwd').send_keys(password_me)
driver.find_element_by_css_selector('#login_btn').click()

driver.get('http://lms.skhu.ac.kr/ilos/mp/course_register_list_form.acl')
# driver.find_element_by_css_selector