'''rsp = '052'


win = {'2': '0', '0': '5', '5': '2'}  # 가위-바위-보 매핑
result = ""  # 최종 문자열을 담을 변수

for i in rsp:           # rsp에서 문자 하나씩 꺼내기
    result += win[i]    # 매핑된 문자 붙이기
print(result)


balls = 6
share = 2
# balls! - (ball - share)!

ball_factorial = 1
for i in range(balls, balls - share):
    ball_factorial *= i

    # share!
share_factorial = 1
for j in range(1, share + 1):
    share_factorial *= j

print(ball_factorial // share_factorial)



numbers = [1, 2, 3, 4, 5, 6]
k = 5

answer = 0
turn = 0

while True:
    for i in numbers[::2]:
        turn += 1
        if turn == k:
            answer.append(i)

            print(answer)
            break
'''


9/22

# 문제1. 책 클래스 만들기


class Book:
    def __init__(self, title, author, total_pages):
        self.title = title            # 책 제목
        self.author = author          # 저자
        self.total_pages = total_pages  # 총 페이지 수
        self.current_page = 0         # 현재 읽은 페이지 초기값은 0

    def read_page(self, pages):
        """주어진 페이지 수만큼 읽되, 총 페이지 수를 넘지 않도록 처리"""
        self.current_page += pages
        if self.current_page > self.total_pages:
            self.current_page = self.total_pages

    def progress(self):
        """읽은 비율을 퍼센트로 소수점 1자리까지 출력"""
        percent = (self.current_page / self.total_pages) * 100
        return f"{percent:.1f}%"


# 사용 예시
my_book = Book("파이썬 입문", "홍길동", 300)
my_book.read_page(50)
print(my_book.progress())  # 16.7%
my_book.read_page(300)
print(my_book.progress())  # 100.0%


# 2 rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width      # 가로
        self.height = height    # 세로

    def area(self):
        """사각형의 넓이를 반환"""
        return self.width * self.height


# 사용자 입력
width = float(input("가로(width)를 입력하세요: "))
height = float(input("세로(height)를 입력하세요: "))

# Rectangle 객체 생성
rect = Rectangle(width, height)

# 넓이 출력
print(f"사각형의 넓이: {rect.area()}")


# 3 비밀번호
class User:
    # 클래스 변수: 생성된 유저 수 저장
    total_users = 0

    def __init__(self, username):
        self.username = username  # 사용자 이름
        self.points = 0           # 포인트 초기값
        User.total_users += 1     # 새로운 유저가 생성될 때마다 1 증가

    def add_points(self, amount):
        """포인트 추가"""
        if amount < 0:
            print("포인트는 음수로 추가할 수 없습니다.")
            return
        self.points += amount

    def get_level(self):
        """포인트 기준 레벨 반환"""
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"

    @classmethod
    def get_total_users(cls):
        """총 유저 수 반환"""
        return cls.total_users


# 사용 예시
user1 = User("Alice")
user2 = User("Bob")

user1.add_points(50)
user2.add_points(150)

print(user1.username, user1.get_level())  # Alice Bronze
print(user2.username, user2.get_level())  # Bob Silver

print("총 유저 수:", User.get_total_users())  # 2


# 성적 검증
class Student:
    def __init__(self, score=0):
        self.__score = 0  # private 변수 초기화
        self.score = score  # setter를 통해 초기값 검증

    @property
    def score(self):
        """점수 getter"""
        return self.__score

    @score.setter
    def score(self, value):
        """점수 setter: 0~100 범위만 허용"""
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("점수는 0 이상 100 이하만 허용됩니다.")


# 사용 예시
student = Student(85)
print(student.score)  # 85

student.score = 95
print(student.score)  # 95

# student.score = 120  # ValueError: 점수는 0 이상 100 이하만 허용됩니다.


# 클래스 오버라이딩


# 부모 클래스 Shape
class Shape:
    def __init__(self, sides, base):
        self.sides = sides  # 변의 개수
        self.base = base    # 밑변의 길이

    def printInfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

# 자식 클래스 Rectangle


class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height  # 높이 추가

    def area(self):
        print(f"사각형 넓이: {self.base * self.height}")

# 자식 클래스 Triangle


class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height  # 높이 추가

    def area(self):
        print(f"삼각형 넓이: {self.base * self.height / 2}")


# 실행 예시
rect = Rectangle(4, 10, 5)
tri = Triangle(3, 8, 6)

print("=== Rectangle 정보 ===")
rect.printInfo()
rect.area()

print("\n=== Triangle 정보 ===")
tri.printInfo()
tri.area()
