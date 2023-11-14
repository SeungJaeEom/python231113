#DemoLoop.py
def cut():
    #절취선 표시
    print("===========================================================================================================================")

# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)
# cut()

value = 5
while value > 0:
    print(value)
    value -= 1
cut()
lst = ["문자열", 100., 3.14]
print(len(lst))
for item in lst:
    print(item)
cut()

#딕셔너리
d = {"apple":100, "orange":200, "kiwi":300}
for k,v in d.items():
    print(k,v)
cut()
d = {"apple":100, "orange":200, "kiwi":300}
for item in d.items():
    print(item)
cut()

lst = list(range(1,11))
print(lst)

years = list(range(2000,2024))
print(years)

days = list(range(1,32))
print(days)

print("----수동으로 반복----")
for i in range(10):
    print(i)

print("----break 구문----")
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("----continue 구문----")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

print("----리스트 함축----")
print([i**2 for i in lst if i > 5])
tp = ("apple", "orange")
print([len(i) for i in tp])
cut()

print("----필터링 함수(X)----")
lst = [10, 25, 30]
itemL = filter(None, lst)
for i in itemL:
    print(i)

#함수 정의
def getBiggerThan20(i):
    return i > 20

print("----필터링 함수(O)----")
itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print(i)

print("----람다 함수----")
itemL = filter(lambda a:a>20, lst)
for i in itemL:
    print(i)

cut()
