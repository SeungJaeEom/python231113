#function3.py
#함수 정의
def cut():
    #절취선 표시
    print("===========================================================================================================================")

def setValue(newValue):
    x = newValue
    print("지역변수:", x)

#함수 호출
retValue =setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

print("----지역변수와 전역변수----")
x = 5
def func1(a):
    return a+x

#호출
print(func1(1))

def func2(a):
    x = 1
    return a+x

#호출
print(func2(1))

print(globals())
print(dir())

cut()
#기본값이 있는 함수
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인지(매개변수명 기술)
def connectUTI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectUTI("multi.com","80"))
print(connectUTI(port="8080",server="multi.com"))
cut()

#가변인자
# union 함수 정의
def union(*ar):
    # 이 함수는 단어를 입력하면 튜플로 받아서
    #유일한 글자를 리스트로 리턴하는 함수입니다.
    result = []
    
    # 입력된 모든 인수에 대해 반복
    for item in ar:
        # 각 인수의 원소에 대해 반복
        for x in item:
            # 결과 리스트에 현재 원소가 없으면 추가
            if x not in result:
                result.append(x)
    
    # 최종 결과 반환
    return result

# 함수 호출 및 결과 출력
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))
cut()

#람다 함수(이름이 없는 간단한 함수 정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
cut()
