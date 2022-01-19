from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(r'C:\Webdriver\chromedriver.exe')
wait = WebDriverWait(browser, 600)
import time
import keyboard

def numcas():
    browser.get("https://covid19.ncema.gov.ae/en")
    casesxpath = "/html/body/main/div[2]/div/div/div[1]/ul/li[4]/div[2]/span"
    cas = browser.find_element_by_xpath(casesxpath).text
    return cas

def nummorts():
    browser.get("https://covid19.ncema.gov.ae/en")
    deathsxpath = "/html/body/main/div[2]/div/div/div[1]/ul/li[5]/div[2]/span"
    morts = browser.find_element_by_xpath(deathsxpath).text
    listemorts = morts.split(" ")
    morts = listemorts[2]
    return morts

def sendwhatsapp():
    cases = numcas()
    deaths = nummorts()
    time.sleep(10)
    browser.get("https://web.whatsapp.com/")
    time.sleep(10)
    NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
    INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
    new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))
    time.sleep(1)
    new_chat_title.click()
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))
    time.sleep(1)
    input_box.send_keys("Coronavirus : COVID-19")
    time.sleep(1)
    input_box.send_keys(Keys.ENTER)
    time.sleep(5)
    keyboard.write("UAE, on ")
    keyboard.write(localtime)
    keyboard.write(" :")
    keyboard.write("\n")
    keyboard.write(cases)
    keyboard.write("\n")
    keyboard.write("New Deaths: ")
    keyboard.write(deaths)
    keyboard.press('enter')

while True:
    localtime = time.asctime(time.localtime(time.time()))
    sendwhatsapp()
    time.sleep(86400)
