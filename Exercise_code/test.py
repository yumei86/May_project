# coding:utf-8
from selenium import webdriver
import time
url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw'
driver = webdriver.Chrome()
driver.delete_all_cookies()  # 開啟瀏覽器時先清除瀏覽器存在的cookie資訊
driver.get(url)     # 進入登入首頁
driver.maximize_window()   # 視窗最大化
cookie1 = driver.get_cookies()   # 獲取登入前cookie
print(cookie1)    # 列印登入前cookie資訊
time.sleep(3)



time.sleep(10)   # 等待10s，利用這段空隙，手動輸入驗證碼

driver.find_element_by_xpath(".//*[@id='login-tabs-item']/div/div[2]/div/div[1]/div/a[1]").click()
time.sleep(3)

cookie2 = driver.get_cookies()   # 獲取登入後cookie
print(cookie2)   # 列印登入後cookie資訊

driver.quit()