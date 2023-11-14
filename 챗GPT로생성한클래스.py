class Person:
    """
    사람을 나타내는 클래스입니다.

    속성:
    - id (int): 사람의 고유 식별자입니다.
    - title (str): 사람의 이름 또는 직책입니다.

    메서드:
    - printInfo(): 사람의 ID와 이름을 출력합니다.
    """

    def __init__(self, person_id, title):
        """
        새로운 Person 인스턴스를 초기화합니다.

        매개변수:
        - person_id (int): 사람의 고유 식별자입니다.
        - title (str): 사람의 이름 또는 직책입니다.
        """
        self.id = person_id
        self.title = title

    def printInfo(self):
        """
        사람의 ID와 이름을 출력합니다.
        """
        print(f"ID: {self.id}, 이름: {self.title}")


class Manager(Person):
    """
    Person 클래스를 상속받아 매니저를 나타내는 클래스입니다.

    속성:
    - skill (str): 매니저의 특정 기술 또는 전문성입니다.

    메서드:
    - printInfo(): 매니저의 ID, 이름, 그리고 기술을 출력합니다.
    """

    def __init__(self, person_id, title, skill):
        """
        새로운 Manager 인스턴스를 초기화합니다.

        매개변수:
        - person_id (int): 매니저의 고유 식별자입니다.
        - title (str): 매니저의 이름 또는 직책입니다.
        - skill (str): 매니저의 특정 기술 또는 전문성입니다.
        """
        super().__init__(person_id, title)
        self.skill = skill

    def printInfo(self):
        """
        매니저의 ID, 이름, 그리고 기술을 출력합니다.
        """
        super().printInfo()
        print(f"기술: {self.skill}")


class Employee(Person):
    """
    Person 클래스를 상속받아 직원을 나타내는 클래스입니다.

    속성:
    - role (str): 직원의 역할 또는 포지션입니다.

    메서드:
    - printInfo(): 직원의 ID, 이름, 그리고 역할을 출력합니다.
    """

    def __init__(self, person_id, title, role):
        """
        새로운 Employee 인스턴스를 초기화합니다.

        매개변수:
        - person_id (int): 직원의 고유 식별자입니다.
        - title (str): 직원의 이름 또는 직책입니다.
        - role (str): 직원의 역할 또는 포지션입니다.
        """
        super().__init__(person_id, title)
        self.role = role


# 샘플 테스트 케이스
# 인스턴스 생성 및 기능 테스트

# 테스트 1 - Person 인스턴스 생성 및 정보 출력
person = Person(1, "존 도우")
person.printInfo()

# 테스트 2 - Manager 인스턴스 생성 및 정보 출력
manager = Manager(2, "제인 스미스", "리더십")
manager.printInfo()

# 테스트 3 - Employee 인스턴스 생성 및 정보 출력
employee = Employee(3, "앨리스 존슨", "개발자")
employee.printInfo()

# 테스트 4 - 다른 Person 인스턴스 생성 및 정보 출력
another_person = Person(4, "마이클 브라운")
another_person.printInfo()

# 테스트 5 - 다른 Manager 인스턴스 생성 및 정보 출력
another_manager = Manager(5, "엠마 데이비스", "커뮤니케이션")
another_manager.printInfo()

# 테스트 6 - 다른 Employee 인스턴스 생성 및 정보 출력
another_employee = Employee(6, "소피아 윌슨", "디자이너")
another_employee.printInfo()

# 테스트 7 - Person 인스턴스 생성 및 정보 출력
person_2 = Person(7, "크리스 리")
person_2.printInfo()

# 테스트 8 - Manager 인스턴스 생성 및 정보 출력
manager_2 = Manager(8, "올리비아 가르시아", "문제 해결")
manager_2.printInfo()

# 테스트 9 - Employee 인스턴스 생성 및 정보 출력
employee_2 = Employee(9, "이단 마르티네즈", "애널리스트")
employee_2.printInfo()

# 테스트 10 - 다른 Person 인스턴스 생성 및 정보 출력
another_person_2 = Person(10, "아바 에른데즈")
another_person_2.printInfo()

p1 = Person(100,"개발자")
p1.printInfo()