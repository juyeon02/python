'''# 게터 세터 실습 1

class UserAccount:
    def __init__(self, username, password):
        self.username = username  # public변수
        self.__password = password  # private변수

    def change_password(self, old_pw, new_pw):
        # 현재 비밀번호가 old_pw와 같을 때만 변경 허용
        if self.__password == old_pw:
            self.__password = new_pw
            print('비번 성공 변경')
        else:
            print('비밀번호 불일치')

    def check_password(self, password):
        # 비밀번호 일치 여부 반환(True/False)

        return self.__password == password


user1 = UserAccount('juyeon', '1234')
print(user1.check_password('1234'))

user1.change_password('juyeon', '133234')
user1 = UserAccount('juyeon', '1234')

# 게터 실습 2

class Student:
    def __init__(self, score=0):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("점수는 0 이상 100 이하만 허용됩니다. ")


s1 = Student(90)
print(s1.get_score())
s1.set_score(80)
print(s1.get_score())


class Student:
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("점수는 0 이상 100 이하만 허용됩니다. ")


# 실습 4. 상속과 오버라이딩
# 문제 1. Shape 클래스 오버라이딩

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f'변의 개수: {self.sides}')
        print(f'밑변의 길이: {self.base}')

    def area(self):
        print(f'넓이 계산이 정의되지 않았습니다.')


class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'사각형 넓이 : {self.base * self.height}')


class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'삼각형 넓이 : {(self.base * self.height) / 2}')


rectangle = Rectangle(4, 10, 5)
triangle = Triangle(3, 10, 5)

rectangle.printInfo()
rectangle.area()

print()

triangle.printInfo()
triangle.area()




# 문제. 추상 클래스 Payment 구현
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")


card = CardPayment()
card.pay(5000)

cash = CashPayment()
cash.pay(3000)
'''
