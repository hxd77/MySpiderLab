from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:#查找table表格内id值为gifList的子标签
    print(child)#find_all没有.children
