import requests
import json
import csv

res = requests.get("https://pm25.lass-net.org/data/history-date.php?device_id=B827EB868D36&date=2020-11-26")
data = json.loads(res.text)
AirBox = map(lambda x: x.get(list(x.keys())[0]) , data['feeds'][0]['MAPS'])
date = map(lambda x: x.get("date", ""), AirBox)
#print(list(date))

AirBox = map(lambda y: y.get(list(y.keys())[0]) , data['feeds'][0]['MAPS'])
time = map(lambda y: y.get("time", ""), AirBox)
#print(list(time))

AirBox = map(lambda z: z.get(list(z.keys())[0]) , data['feeds'][0]['MAPS'])
T = map(lambda z: z.get("s_t0", ""), AirBox)
#print(list(T))


AirBox = map(lambda z: z.get(list(z.keys())[0]) , data['feeds'][0]['MAPS'])
CO2 = map(lambda z: z.get("s_g8", ""), AirBox)
#print(list(CO2))

a = []
b = []
c = []
d = []
for item in list(date): 
    a.append(item)
for item in list(time): 
    b.append(item)
for item in list(T): 
    c.append(item)
for item in list(CO2): 
    d.append(item)


ans = ['','',0,0]
with open('11_26.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=',') #以空白分隔欄位，建立 CSV 檔寫入器
    writer.writerow(['date','time','T','CO2'])
    for i in range(len(a)):
        ans[0] = a[i]
        ans[1] = b[i]
        ans[2] = c[i]
        ans[3] = d[i]
        writer.writerow([ans[0],ans[1],ans[2],ans[3]])

        



