import requests
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now().timestamp())#表示unix时间戳
proxies={
    "http":'http://127.0.0.1:7897',
    "https":'http://127.0.0.1:7897'
}

headers={"User-Agent":"Mozilla/5.0"}

url="https://en.wikipedia.org/wiki/Kevin_Bacon"
resp=requests.get(url=url,headers=headers,proxies=proxies)
bs=BeautifulSoup(resp.text,'html.parser')
for link in bs.find_all('a'):#links是一个包含标签<a>的列表
    #print(link.attrs)
    if 'href' in link.attrs:#判断这个字典有没有href属性
        print(link.attrs['href'])