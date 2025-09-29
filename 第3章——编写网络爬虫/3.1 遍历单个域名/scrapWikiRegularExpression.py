import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now().timestamp())

proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"
}

headers = {"User-Agent": "Mozilla/5.0"}

def getLinks(articleUrl):
    """
    获取 Wikipedia 指定文章的内部链接
    - href 以 /wiki/ 开头
    - 不包含冒号 :
    """
    resp = requests.get(url=f'https://en.wikipedia.org{articleUrl}', headers=headers, proxies=proxies)
    bs = BeautifulSoup(resp.text, 'html.parser')
    links = bs.find('div', {'id': 'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$')#属性可以写成字典
    )
    """在刚找到的 <div> 里面，再找所有 <a> 标签（超链接）。

href=re.compile('^(/wiki/)((?!:).)*$') 用正则表达式过滤：

^(/wiki/) ：要求链接以 /wiki/ 开头（维基百科的词条链接都这样）。

((?!:).)* ：这是一个 负向前瞻，意思是匹配的内容里不能出现 :。

因为像 Category:XXX、File:XXX 这样的链接不是正常词条，所以要排除掉。

$ ：字符串结尾开始匹配"""
    return links

links = getLinks('/wiki/Kevin_Bacon')
#links是一个包含<a>标签的列表
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']#找出<a>标签中的href属性
    print(newArticle)
    links=getLinks(newArticle)

