import os
import time
import requests
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Webdriver\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(10)
input('Ready to Start Track')


ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'
status = 'off'


def check_status():
    try:
        driver.find_element_by_xpath(ONLINE_STATUS_LABEL)
        return True
    except:
        return False

def calculate_time(t):
    if t < 60:
        return(str(t)+'s')
    else:
        return(str(t // 60)+'min ', str(t % 60)+'s')


while(True):
    time.sleep(2)
    localtime = time.asctime(time.localtime(time.time()))
    if check_status() and status == 'off':
        print('Online')
        with open('online.txt', 'a') as f:
            f.write('\n')
            f.write('Online on ' + localtime)
        time_1 = time.time()
        status = 'on'
    if not check_status() and status == 'on':
        print('Offline')
        time_2 = time.time()
        time_interval = time_2 - time_1
        status = 'off'
        with open('online.txt', 'a') as f:
            f.write('\n')
            f.write('Offline on ' + localtime)
            f.write('\n')
            f.write('Session time : '+ calculate_time(int(time_interval)))
            f.write('\n')
