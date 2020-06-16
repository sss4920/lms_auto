from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from datetime import datetime
import time
import schedule

def edu_auto():
    driver = webdriver.Chrome()
    url = 'http://lms.skhu.ac.kr/ilos/main/main_form.acl'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    driver.find_element_by_css_selector('.header_login.login-btn-color').click()
    f=open("mytext.txt","r")
    id_me = "id 입력하자"
    password_me = "pass 입력하자"
    week=14                 # 나중에 원하는 주차로 자동으로 date를 활용해 설정
    second_count = 0
    loopcount = 1
    educate_number = 0
    for line in f.readlines():
        if loopcount ==1:
            id_me = line
            loopcount+=1
        else:
            password_me = line

    # login user
    action.send_keys(id_me).perform()
    driver.find_element_by_css_selector('#usr_pwd').send_keys(password_me)
    driver.find_element_by_css_selector('#login_btn').click()
    time.sleep(2)

    # educate auto
    driver.get('http://lms.skhu.ac.kr/ilos/mp/course_register_list_form.acl')
    for x in range(len(driver.find_elements_by_css_selector('.content-title'))):  # 해당주차의 1강 2강 같은거 있으면 그거 반복
        driver.find_elements_by_css_selector('.content-title')[educate_number].click()
        driver.find_element_by_css_selector('#week-{}'.format(week)).click()
        time.sleep(2)

        driver.find_element_by_css_selector('.view').click()
        time.sleep(5)
        pyautogui.typewrite(['enter'])
        if len(driver.find_elements_by_css_selector('.item-title-lesson.item-title-lesson-on')) > 1:
            for x in driver.find_elements_by_css_selector('.item-title-lesson.item-title-lesson-on'):  # 교시가 있으면 그거 누름
                x.click()
                while True:
                    time.sleep(1)
                    second_count += 1
                    print(second_count)
                    if second_count == 3600:
                        break
        else:
            while True:
                time.sleep(1)
                second_count += 1
                print(second_count)
                if second_count == 3600:
                    break
        driver.find_element_by_css_selector('#close_').click()
        driver.get('http://lms.skhu.ac.kr/ilos/mp/course_register_list_form.acl')
    driver.close()

schedule.every().tuesday.at("22:23").do(edu_auto)
# driver.find_element_by_css_selector

while True:
    schedule.run_pending()
    time.sleep(1)