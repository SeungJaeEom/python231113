#DB1.py

import sqlite3

#메모리에서 작업
#연결객체 리턴받기
con = sqlite3.connect(":memory:") #테스트할때 사용, 메모리에 올려서 사용할 때 ":memory:" 라고 적는다.
#커서객체 리턴
cur = con.cursor()

#테이블구조(자료구조 생성)
cur.execute("create table PhoneBook (name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('홍길동','010-222');")

#입력 파라메터 처리
name = "전우치"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#N건을 입력
dataList = (("박문수","010-333"),("김길동","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", (dataList))

#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

print("----feetchone()----")
print(cur.fetchone())
print("----feetchmany(2)----")
print(cur.fetchmany(2))
print("----feetchall()----")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())