# 클래스
'''
클래스는 객체를 만들기 위한 설계도 입니다.
클래스 = 붕어빵 틀
객체(인스턴스) = 실제로 만들어진 붕어빵

클래스를 사용하면 관련된 데이터와 기능을 하나로 묶어서 관리

'''

# 클래스 사용 목적
"""
1. 코드 재사용성 : 한번 작성한 코드를 여러 곳에서 활용
2. 유지보수 용이ㅣ 수정사항이 있을 때 클래스만 수정하면 됨
3. 코드 구조화ㅣ 복잡한 프로그램을 체계적으로 구성
4. 현실 세꼐 모델링: 실제 사물이나 개념을 프로그램으로 표현

"""

'''# 클래스 사용 방법


class 클래스_이름:
    def __init__(self):
        pass

    def 메서드이름(self):
        # 메서드 코드
        pass


class Car:
    def __init__(self, brand model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, increase):
        # 속도를 증가시키는 매서드
        self.spped += increase
        print(f'속도가{increase}km/h 증가했습니다. 현재 속도 : {self.speed}km/h')

    def brack(self, decrease):
        # 속도를 감소시키는 매서드

        self.speed = max(0, self.speed-decrease)  # 속도는 0 미만이 될 수 없다
        print(f'속도가{increase}km/h 감소했습니다. 현재 속도 : {self.speed}km/h')

    def info(self):
        # 차량 정보를 출력하는 메서드
        print(f'{self.brand}')
        print(f'{self.model}')
        print(f'{self.color}')
        print(f'{self.speed}')


# 객체 생성 및 사용
my_car = Car('tesla', 'model 3', '빨간색')
# my_cal 객체(인스턴스)의 정보 출력

my_car.info()
my_car.accelerate(80)
my_car.brack(30)
my_car.info
'''

'''
class Students:
    def __init__(self, name, age, student_id):
        # 생성자ㅣ 학생 객체 초기화
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        print(f'학생{name}의 정보 등록')

    def add_grade(self, grade):
        # 성적 추가 메서드
        self.grades.append(grade)
        print(f'{self.name}의 성적 {grade}점이 추가되었습니다')

    def get_averate(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)

        return 0

    def __del__(self):
        # 소멸자
        # 객체가 메모리에서 삭제될 때 호출되는 메서드
        print(f'{self.name}이 사라졌습니다. ')


# 객체(인스턴스) 생성
student1 = Students('김철수', 20, '20240001')
student1.add_grade(70)
student1.add_grade(60)


student2 = Students('이영희', 22, '20230001')
print('평균점수', student1.get_averate())


# 인스턴스 변수, 클래스 변소

인스턴스 변수 : 각 객체마다 독립적으로 가지는 변수
클래스 변수 : 모든 객체가 공유하는 변수



class BankAccount:
    # 클래스 변수
    bank_name = '파이썬 은행'
    total_accounts = 0
    interset_rate = 0.02   # 이자율

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.total_accounts + 1
        # 클래스 변수 업데이트

        BankAccount.total_accounts += 1

    def deposit(self, amount):
        # 입금 메서드
        if amount > 0:
            self.balance += amount
            print(f'{amount}원이 입금 되었습니다. 잔액 : {self.balance}원')

    def withdraw(self, amount):
        # 출금 메서드
        if self.amount >= amount:
            self.balance -= amount
            print(f'{amount}원이 출금 되었습니다. 잔액 : {self.balance}원')
        else:
            print('잔액 부족')

    def apply_interest(self):
        # 이자 적용
        interest = self.balance * BankAccount.interset_rate
        self.balance += interest
        print(f"dlwk {interest}원이 적용")

    @classmethod
    def change_interest_rate(cls, new_rate):
        # 클래스 메서드 이자율 변경
        cls.interset_rate = new_rate
        print(f'이자율 {new_rate*100}% 로 변경 되었습니다. ')

    def __del__(self):
        BankAccount.total_accounts -= 1
        print('계좌 삭제')


account1 = BankAccount('홍길동', 10000)
account2 = BankAccount('김철수', 15000)

print(f'은행이름: {BankAccount.bank_name}')
print(f'총 계좌 수 : {BankAccount.total_accounts}')
print(f'number {BankAccount.total_accounts}')

account1.deposit(5000)  # 입금
account2.apply_interest()  # 이자 적용


class Calculator:
    Calculation_count = 0

    def __init__(self, name):
        self.name = name
        self.history = []

    def add_to_history(self, operation, result):
        # 계산 기록 저장
        self.history.append(f'{operation} = {result}')
        Calculator.Calculation_count += 1

    @classmethod
    def get_total_calcultions(cls):
        # 전체 계산 횟수 반환
        return cls.Calculation_count

    @staticmethod
    def add(a, b):
        # 두 수의 합
        return a + b

    @staticmethod
    def multiply(a, b):
        # 두 수의 곱
        return a * b

    @staticmethod
    def is_even(number):
        is 로 시작되는 함수는 대부분 불리언으로 반환
        # 짝수 판별
        return number % 2 == 0

    def calculate_and_save(self, a, b, operation):
        # 계산하고 기록 저장
        if operation == 'add':
            result = self.add(a, b)
            self.add_to_history(f'{a} + {b} , result')

        elif operation == 'multiply':
            result = self.multiply(a, b)
            self.add_to_history
        return result


calc1 = Calculator('계산기1')
calc2 = Calculator('계산기 2')

# 정적 메서드 사용(인스턴스 없이도 호출 가능)
print(Calculator.add(5, 3))
print(Calculator.is_even(5))

# 인스턴스 메서드 사용
result = calc1.calculate_and_save(10, 20, "add")
print(f'결과 : {result}')

# 클래스 메서드 사용
print(f'총 계산 횟수: {Calculator.get_total_calcultions()}')


# 접근 제어자

객체 지향 프로그래밍에서 클래스의 멤버(속성, 메서드)에 대한 접근 권한을 제어하는 메커니즘

파이썬의 철학:
파이썬은 프로그래머를 신뢰하는 철학을 가짐
강제적 제한보다는 컨벤션과 문서화를 중시
필요하다면 모든 것에 접근 가능(하지만 하지 말아야 할 것을 명확히 표시)




class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        # 외부에서 자유롭게 호출 가능
        self.speed += amount
        return f'속도가 {self.speed}km/h 가 되었습니다'

    def get_info(self):
        return f'{self.brand}{self.model}'


# 객체 생성
car = Car('tesla', 'model 3')
print(car.model) # 정상 접근
print(car.brand) # 정상 접근
print(car.get_info()) # 정상호출
car.speed = 200 # 직접 수정 가능 

# private 속성/메서드(언더스코어 2개 __)



class SecuritySystem:
    
    return self._failed _attempts < 3
    def authenticate(self, password): #public 메서드
        if not self._check_security(): # private 메서드 호출
            return "계정이 잠겼습니다."

# 인자로 받은 pass
encrypted = Self._encrypt_password(password) # private 메서드 호출
if encrypted == self. encrypt_password(self._ password):
self._ failed attempts = 0
return '인증 성공'
else:

self._failed_attempts += 1
return f 인증 실패 {self._failed_attempts}/3'

security = SecuritySystem ('secret123')
# print(security._password)
# security..
_check_ security()

'''

# propety를 사용하지 않은 경우


class Circle1:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius


c1 = Circle1(5)
print(c1.get_area())

c2 = Circle2(4)
print(c2.area)


class Vector:
    def __init__(self):
        # 생성자: 속성초기화
        pass

    def __str__(self):
        # print()함수 호출시
        return f 'Vector{}{}'

    def __repr__(self):
        # 개발자를 위한 문자열 표현
        retyrn f'Vector(x = {self.x} y = {self.y})'

    # 연산자 오버로딩
    def __add__(self, other):
        # + 연산 오버로딩
        return Vector(self.x + other.x, self.y + other.y)

    # __sub__,  __mul__, __eq__

    def __len__(self):
        # len()함수 호출시
        return int(self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(V1)
