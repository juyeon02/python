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

# 실습2. math모듈 사용해보기
# 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기
import time
import os
import sys
import datetime
import random
import math

# 좌표 입력받기
x1, y1 = input("(x1, y1) 를 입력하세요 : ").split(",")
x2, y2 = input("(x2, y2) 를 입력하세요 : ").split(",")

x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

# 두 점 사이 거리 계산
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f'실제 거리: , {distance: .2f}')


# 문제 2. 상품 나누기: 최소 공배수와 최대 공약수


print(f'최대 공약수: {math.gcd(18, 24)}')
print(f'최소 공배수: {math.lcm(18, 24)}')


# 실습3. 로또 번호 뽑기
num = set()

while len(num) < 6:
    num.add(random.randint(1, 45))

print(sorted(num))


# 가위 바위 보 게임
pc = ['가위', '바위', '보']
user = input('가위, 바위, 보 중 하나를 입력하세요: ')

pc_choice = random.choice(pc)
print(f'pc 선택: {pc_choice}')

if pc_choice == user:
    print('무승부')

elif ((user == '가위' and pc_choice == '보') or
      (user == '바위' and pc_choice == '가위') or
      (user == '보' and pc_choice == '바위')):
    print('사용자 승!')

else:
    print('패')


# 실습5. 다음 생일까지 남은 날짜 계산하기


birthday = input('월-일을 입력하세요 : ').split("-")
month = int(birthday[0])
day = int(birthday[1])


birthday = datetime.date(2025, month, day)

today = datetime.date.today()
print(today)

if birthday < today:
    birthday = datetime.date(2026, month, day)


d_day = birthday - today

print(f'{d_day.days} 일')

# sys
x = input("수 입력: ")
n = int(x)

if n == 0:
    print("0으로 나눌 수 없습니다")
    sys.exit(0)

result = 10/n
print(result)


# os

# 1. 현재 작업 디렉터리 확인
print("현재 작업 디렉터리: ", os.getcwd())

# 2. 새 폴더 생성 (이미 있으면 예외 발생 가능)
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"{folder_name} 폴더를 생성했습니다.")

else:
    print(f'{folder_name} 폴더가 이미 존재합니다')

# 3. 현재 디렉터리 내 파일/ 폴더 목록 출력
print("현재 디렉터리 내 파일 및 폴더 목록: ")
print(os.listdir())


# 실습6. 타자 연습 게임 만들기


word = ['moon', 'potato', 'sky', 'garlic']    # 1. 영단어 리스트 중 무작위로 단어가 제시됩니다.
word_choice_number = 1
user_answer = 0

start = time.time()   # 수행 시간 측정하기

input('엔터를 누르면 게임이 시작됩니다.: ')

while user_answer < 10:
    word_choice = random.choice(word)

    while True:
        print(f'{word_choice_number}번 문제 :  {word_choice}')
        user = input("단어를 입력하세요: ")   # input()으로 사용자 입력

        if word_choice == user:
            user_answer += 1
            print('통과')
            word_choice_number += 1
            break
        else:
            print('오타! 다시 도전!')


end = time.time()
print(f'"타자 시간 : {end-start: .2f} 초')
