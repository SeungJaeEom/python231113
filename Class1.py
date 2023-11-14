#Class1.py
#1)클래스를 정의

class Person:
    #초기화 메서드
    def __init__(self): #__init__는 초기화 메서드로 기본 클래스 함수에 정의되어 있음(java의 생성자와 같음). self는 java의 this와 같지만 키워드는 아님
        self.name = "default name" #name은 클래스의 멤버 변수
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스를 정의
p1 = Person() #파이썬에서는 새로운 객체를 만들때 new 라는 키워드는 사용하지 않는다.
p2 = Person()
p1.name = "전우치"

#3)메서드 호출
p1.print()
p2.print()

#런타임(코드가 실행중)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
