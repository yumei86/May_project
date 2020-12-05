from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

#inp = input()

driver = webdriver.Chrome()
driver.get('https://irs.thsrc.com.tw/IMINT/?locale=tw')
driver.maximize_window()
cookie1 = driver.get_cookies()   # 獲取登入前cookie
print(cookie1)    # 列印登入前cookie資訊

#移到網路訂票
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/table/tbody/tr/td/input').click()


#選出發站
b = driver.find_element_by_xpath('//select')
b.click()
select = Select(driver.find_element_by_name('selectStartStation'))
select.select_by_visible_text(u"台北")

#選到達站
c = driver.find_element_by_xpath('//td[2]/select')
c.click()
select_c = Select(driver.find_element_by_name('selectDestinationStation'))
select_c.select_by_visible_text(u"新竹")

#輸入年月日
driver.find_element_by_xpath('//tr[5]/td[2]/span/input').click()
driver.find_element_by_xpath('//tr[5]/td[2]/span/input').send_keys(Keys.COMMAND+'A')

driver.find_element_by_xpath('//tr[5]/td[2]/span/input').send_keys('2020/11/27')


driver.find_element_by_xpath('//span[2]/select').click()
Select(driver.find_element_by_name('toTimeTable')).select_by_visible_text(u"12:00")

time.sleep(10)

driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/table/tbody/tr/td[2]/input[2]').click()

time.sleep(3)

cookie2 = driver.get_cookies()   # 獲取登入後cookie
print(cookie2)