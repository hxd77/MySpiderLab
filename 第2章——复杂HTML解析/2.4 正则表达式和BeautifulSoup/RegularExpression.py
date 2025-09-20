from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('http://pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')
images=bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts\/img.\.jpg')})
#print(images) images是一个列表，里面包含[<img src="../img/gifts/img1.jpg"/>, <img src="../img/gifts/img2.jpg"/>, <img src="../img/gifts/img3.jpg"/>, <img src="../img/gifts/img4.jpg"/>, <img src="../img/gifts/img6.jpg"/>]
for image in images:
    print(image)
    
