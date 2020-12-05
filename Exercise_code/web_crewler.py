import requests
from bs4 import BeautifulSoup

#請求目標網站
re = requests.get("https://www.ccclub.io/course/2020Fall")
print(re.status_code)

#解析網站 re.text是網頁原始碼
soup = BeautifulSoup(re.text, 'html.parser')
#print(soup.title)
#print(soup.title.string)

#處理表格
results = soup.tbody
#print(results)
c = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['container'])
for data in c:
    print(data)
#for tr in results.find_all('tr'):
#    print(tr.find_all('td')[0].text)