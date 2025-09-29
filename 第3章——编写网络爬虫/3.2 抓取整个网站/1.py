import requests
from bs4 import BeautifulSoup
import re

proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"
}
headers = {"User-Agent": "Mozilla/5.0"}
pages= set()#用来存储已经访问过的页面
def getLinks(pageUrl):
    global pages #全局作用域
    resp=requests.get(url=f"https://en.wikipedia.org{pageUrl}",headers=headers,proxies=proxies)
    bs=BeautifulSoup(resp.text,'html.parser')
    for link in bs.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        #print(link.attrs)#是一个字典
        if 'href' in link.attrs:#有些<a>标签没有href属性
            if link.attrs['href'] not in pages:#如果没有访问过
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)#递归调用
                
getLinks("")#从首页开始抓取