
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import pyautogui


#-------將網頁開啟的動作換為背景執行----------

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-automation'])  #把新版google的自動控制提醒關掉
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(executable_path='chromedriver',options=options)
link = 'https://www.google.com/maps/d/u/0/viewer?fbclid=IwAR3O8PKxMuqtqb2wMKoHKe4cCETwnT2RSCZSpsyPPkFsJ6NpstcrDcjhO2k&mid=1I8nWhKMX1j8I2bUkN4qN3-FSyFCCsCh7&ll=24.807740000000006%2C120.96740199999999&z=8'
driver.get(link)

time.sleep(3)


#-------關掉即將開幕的選單-------
first_cl = driver.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]")
first_cl.click()

#-------下滑網頁(較南邊的縣市需要)-------
#pyautogui.scroll(-10)

#-------把[台北基隆]剩下項目打開-------(這邊可以看你要怎麼爬去改縣市的參數）
start_search_btn = driver.find_element_by_xpath("//div[2]/div/div[3]/div[2]/div/div")
start_search_btn.click()


#-------打開[台北]第一間評論(要記得關掉)-------（這邊可以看你要怎麼爬去改縣市的參數）
driver.find_element_by_xpath("//div[2]/div/div[3]/div[3]/div[2]/div").click()
time.sleep(3)


#下面打開為範例 可以依照你爬的東西去改
#-------打開台北第一間評論---------
#store = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="suEOdc"]')))
s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([i.text for i in s1])

driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(1)

#-------打開台北第二間評論---------
driver.find_element_by_xpath("//div[2]/div/div[3]/div[4]/div[2]/div").click()
time.sleep(1)

s2 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([j.text for j in s2])

driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(1)

#-------打開台北第三間評論---------
driver.find_element_by_xpath("//div[2]/div/div[3]/div[5]/div[2]/div").click()
time.sleep(1)

s3 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([j.text for j in s3])

#-------[你的部分的名稱]---------