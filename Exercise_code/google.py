from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-automation'])  #把新版google的自動控制提醒關掉
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(executable_path='chromedriver',options=options)
link = 'https://www.google.com/'
driver.get(link)
search_input = driver.find_element_by_name("q")
search_input.send_keys('笑話')
time.sleep(3)

start_search_btn = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
start_search_btn.click()

