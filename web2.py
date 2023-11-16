#web2.py
#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

#당근마켓
url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
f = open("dangn.txt","wt", encoding="utf-8")

posts = soup.find_all("div",attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2",attrs={"class":"card-title"})
    price = post.find("div",attrs={"class":"card-price"})
    addr = post.find("div",attrs={"class":"card-region-name"})

    title = title.text.replace("\n","").strip()
    price = price.text.replace("\n","").strip()    
    addr = addr.text.replace("\n","").strip()    
    
    print("{0}|{1}|{2}".format(title, price, addr).strip())
    f.write(f"{title},{price},{addr}\n")

f.close()

# <div class="card-desc">
#       <h2 class="card-title">네이버페이44만원 싸게팝니다</h2>
#       <div class="card-price ">
#         400,000원
#       </div>
#       <div class="card-region-name">
#         경기도 부천시 춘의동
#       </div>
