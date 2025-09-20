from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:#返回table表格中的第一个tr的同级兄弟节点不会返回第一个tr标签
    print(sibling)