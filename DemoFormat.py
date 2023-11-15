#DemoFormat.py
def cut():
    #절취선 표시
    print("===========================================================================================================================")

# for i in range(1,11):
#     URL = "http://multi.com/?page=" + str(i)
#     print(URL)

# cut()

# print("----숫자 출력----")
# for x in range(1,6):
#     print(x,"*",x,"=",x*x)

# print("----오른쪽 정렬----")
# for x in range(1,6):
#     print(x,"*",x,"=",str(x*x).rjust(3))

# print("----0으로 채우기----")
# for x in range(1,6):
#     print(x,"*",x,"=",str(x*x).zfill(5))
#cut()

#파일 쓰기
#r을 넣는 이유: \\ 를 사용하지 않고 \ 하나만 사용하도록 할 때 넣어줌(Raw String Notation)
f = open(r"c:\work\test.txt","wt",encoding="utf-8") 
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close()

#파일에 첨부(a+ : append, read, write)
f = open(r"c:\work\test.txt","a+",encoding="utf-8")
f.write("추가로 첨부하기\n")

#파일 읽기
f = open(r"c:\work\test.txt","rt",encoding="utf-8")
print(f.read())
#f.close()

#다시 처음으로 리셋
f.seek(0)
result = f.readlines()
#end="" 사용하는 이유는 print 사용시 기본적으로 새로운 라인을 추가 하는데 
#위 소스에서 \n을 넣어서 줄바꿈이 두번 되기 때문에 두번 줄바꿈을 없애려고 사용함
for item in result:
    print(item, end="") 

#다시 처음
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.close()
cut()

#서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))