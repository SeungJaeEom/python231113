#web1.py
#웹 크롤릴을 위한 선언
from bs4 import BeautifulSoup #from 뒤는 폴더(패키지), import 뒤는 모듈(파일)

#페이지 로딩
page = open("test01.html","rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 페이지 보기
#print(soup.prettify())

#<p>전체를 검색
#print(soup.find_all("p"))
#첫번째<p>만 검색
#print(soup.find("p"))
#조건검색:<p class="outer-text">
#class 키워드와 충돌
#print(soup.find_all("p", class_="outer-text")) #class 자체가 파이썬의 키워드라서 class_ 라고 해준다.
#attrs속성
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#<p id="first">인거 찾기
#print(soup.find_all("p", id="first"))
#태그 안쪽의 컨텐츠만 출력: .text 속성
for tag in soup.find_all({"p","href"}):
    title = tag.text.strip()
    title = title.replace("\n","")
    title = title.replace("                                ","\n")
    print(title)
