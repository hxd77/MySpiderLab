import requests
from bs4 import BeautifulSoup
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')


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
    try:
        print(bs.h1.get_text())#打印h1中的纯文本标题
        print(bs.find(id='mw-content-text').find_all('p')[0])#find_all('p')返回一个列表,打印正文的第一个段落
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])#打印编辑链接
        """类似于
        <li id="ca-edit">
        <span>
            <a href="/w/index.php?title=Python&action=edit">编辑</a>
        </span>
        </li>
        """
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")
    for link in bs.find_all('a',href=re.compile('^(/wiki/)')):
        #link类似于<a href="/wiki/Russell_M._Nelson" title="Russell M. Nelson">Russell M. Nelson</a>
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新页面
                newPage=link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)#递归调用
getLinks("")#从首页开始抓取