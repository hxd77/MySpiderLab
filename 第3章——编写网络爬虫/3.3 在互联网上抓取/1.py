import requests
from bs4 import BeautifulSoup
import re
import datetime
import random
import sys
from urllib.parse import urlparse
from urllib.request import urlopen
sys.stdout.reconfigure(encoding='utf-8')

random.seed(datetime.datetime.now().timestamp())
proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"}
headers={"User-Agent":"Mozilla/5.0"}


#获取页面中所有内链的列表
def getInternalLinks(bs,includeUrl):
    includeUrl=f'{urlparse(includeUrl).scheme}://{urlparse(includeUrl).netloc}'
    print(includeUrl)
    #includeUrl = 'https://en.wikipedia.org'类似
    """urlparse 是 Python 标准库 urllib.parse 提供的函数。它可以把 URL 拆解成 6 个部分：.scheme表示 URL 的协议，比如 http、https。
    .netloc表示IP地址"""
    internalLinks = []
    #找出所有以"/"开头的链接"
    for link in bs.find_all('a',href=re.compile('^(/|.*'+includeUrl+')')):#匹配 空字符串 或者 任何包含 includeUrl 的字符串。
        #例如^(/|.*wikipedia.org)
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    '''如果 href 以 / 开头，说明它是一个相对路径（比如 /wiki/Python），属于当前网站内部链接。
                    如果不是 / 开头（比如 https://google.com），就不是内部链接。'''
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
                return internalLinks

#获取页面中所有外链的列表
def getExternalLinks(bs,excludeUrl):
    externalLinks=[]
    #找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bs.find_all('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):#匹配 以 http 或 www 开头，且不包含 excludeUrl 的字符串。
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    resp=requests.get(url=startingPage,headers=headers,proxies=proxies)
    bs=BeautifulSoup(resp.text,'html.parser')
    externalLinks=getExternalLinks(bs,urlparse(startingPage).netloc)
    if len(externalLinks)==0:
        print("No external links, looking around the site for one")
        domain=f'{urlparse(startingPage).scheme}://{urlparse(startingPage).netloc}'
        internalLinks=getInternalLinks(bs,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
        #随机返回一个内链
    
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink(startingSite)
    print(f"Random external link is: {externalLink}")
    followExternalOnly(externalLink)
followExternalOnly("http://oreilly.com")#从O'Reilly开始抓取
