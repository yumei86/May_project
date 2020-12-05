from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import csv
import pyautogui



#-------將網頁開啟的動作換為背景執行----------

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-automation'])  #把新版google的自動控制提醒關掉
#options.add_argument("window-size=1920,1080")
#options.add_argument("--start")
driver = webdriver.Chrome(executable_path='chromedriver',options=options)
link = 'https://www.google.com/maps/d/u/0/viewer?fbclid=IwAR3O8PKxMuqtqb2wMKoHKe4cCETwnT2RSCZSpsyPPkFsJ6NpstcrDcjhO2k&mid=1I8nWhKMX1j8I2bUkN4qN3-FSyFCCsCh7&ll=24.807740000000006%2C120.96740199999999&z=8'
driver.get(link)

time.sleep(3)


#-------關掉即將開幕的選單-------
first_cl = driver.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]")
first_cl.click()

#-------下滑網頁(較南邊的縣市需要)-------
#pyautogui.scroll(-10)

#-------把[台北基隆]剩下項目打開--------
start_search_btn = driver.find_element_by_xpath("//div[2]/div/div[3]/div[2]/div/div")
start_search_btn.click()


store_name = []
store_loca = []

#-------打開[台北基隆]評論爬名字(要記得關掉)-------
for items in range(2):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[2]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)

    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    print(s1[1].text.split("\n"))
    store_name.append(s1[0].text)
    
    try:
        location = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="fO2voc-jRmmHf-MZArnb-Q7Zjwb"]')))
        print(location[0].text)
        store_loca.append(location[0].text) 
    except:
        store_loca.append("無提供地址資訊")

    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)

'''
ans = ['','']
with open('Ramen_name.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=',') #以空白分隔欄位，建立 CSV 檔寫入器
    writer.writerow(['name','address'])
    for i in range(len(store_name)):
        ans[0] = store_name[i]
        ans[1] = store_loca[i]
        writer.writerow([ans[0],ans[1]])
'''
driver.close() #關掉瀏覽器