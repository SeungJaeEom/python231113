#[] <- 브라켓, list 선언할때 사용
#DemoListTuple
#리스트에 추가할 경우 += [] 으로 묶어야 함. 아래 소스는 잘못 코딩된것
#리스트에 추가할 경우 ~.append()를 사용하는 것이 좋음
#ctrl + F5 누르면 실행

colors = ["red","blue","green"]
print(len(colors))
print(type(colors))
colors.append("white")
colors.insert(1,"pink")
print(colors)
colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors)
colors.remove("red")
print(colors)
colors.extend(["black","yellow","green"])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

#* 하나는 튜플
#** 두개는 Dict
#파이썬 코딩시 자주 사용하는 타입 : list(), int(), str(), range()

#디버깅할 때 중단점(Break Point)
for item in colors:
    print(item)


print("----set형식----")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("----tuple형식----")
tp = (10,20,30)
print(len(tp))
print(type(tp))

#함수정의 def 함수명(args): 
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)
print(result[0])
print(result[1])

print("id:%s, name:%s" %("kim","김유신"))

args = (5,6)
print(calc(*args)) # *표시를 붙여서 tuple이라고 명시해야함

#변수는 ()가 없음, 함수는 반드시 ()가 있음
#위 예제 중 calc는 함수, result나 args는 변수
#블럭단위 주석처리를 할 경우 블럭을 잡고 ctrl + / 누르면 해당 블럭에 주석처리됨

print("----형식변환----")
a = set((1,2,3))
print(a)
b = list(a)
print(b)
b.append(4)
print(b)

#dict는 맵핑 구조로서 key:value 형식으로 구성되어 있다.
#1. ~.items(): key + value
#2. ~.keys(): key만
#3. ~.values(): value만

