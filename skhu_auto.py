from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from datetime import datetime
import time
import schedule
from bs4 import BeautifulSoup

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
    for x in range(len(driver.find_elements_by_css_selector('.content-title'))):  # 강의 선택 ex 교양시사영어
        driver.find_elements_by_css_selector('.content-title')[educate_number].click()
        driver.find_element_by_css_selector('#week-{}'.format(week)).click()
        time.sleep(2)

        # 여기에도 .view를 크롤링해서 클릭할때 여러개의 강의목록이 나올수있어서 추가요함
        driver.find_element_by_css_selector('.view').click()
        time.sleep(5)
        pyautogui.typewrite(['enter'])
        time.sleep(2)
        if len(driver.find_elements_by_css_selector('.item-title-lesson')) > 1:
            print("교시가 있습니다.")
            class_time = driver.find_elements_by_css_selector('.item-title-lesson')

            time_room=0
            for x in range(len(class_time)):
                while True:
                    time.sleep(1)
                    second_count += 1
                    print(second_count)
                    if second_count == 50:
                        break
                second_count=0
                time_room +=1
                class_time[time_room].click()
                time.sleep(5)
                pyautogui.typewrite(['enter'])
        else:
            print("교시가 없는 경우로 들어옵니다.")
            while True:
                time.sleep(1)
                second_count += 1
                print(second_count)
                if second_count == 50:
                    break
            second_count=0
        driver.find_element_by_css_selector('#close_').click()
        time.sleep(5)
        pyautogui.typewrite(['enter'])
        driver.get('http://lms.skhu.ac.kr/ilos/mp/course_register_list_form.acl')
        educate_number+=1
    driver.close()

schedule.every().wednesday.at("14:13").do(edu_auto)




while True:
    schedule.run_pending()
    time.sleep(1)