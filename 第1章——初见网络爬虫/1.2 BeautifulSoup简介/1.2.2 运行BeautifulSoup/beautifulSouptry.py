from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page1.html')  
bs=BeautifulSoup(html,'html.parser')     #html.read()获取网页的HTML内容 ,html.parser表示python解析器
print(bs.h1)