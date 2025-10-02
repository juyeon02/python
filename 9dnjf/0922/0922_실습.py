'''
# 문제1. 책 클래스 만들기

class Book:
    def __init__(self, title, author, total_pages,):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def read_page(self, pages):
        if pages < 0:
            return

        self.current_page = min(self.total_pages, self.current_page + pages)

    def progress(self):
        pct = (self.current_page / self.total_pages) * 100
        return round(pct, 1)

     roud:  소숫점(, 1)  1자리까지 출력하겠다 

    def __repr__(self):
        return f "<Book {self.title} by {self.author}>"

    # 객체 생성
    b = Book('파이썬 클린코드', '홍길동', total_pages=320)
    b.read_page(100)
    print(b)
    print(b.progress(), '%')
    b.read_page(1000)
'''


# 문제2. Rectangle 클래스 구현
'''
▪ 메서드:
• area() : 사각형의 넓이 반환

▪ 사용자 입력:
• 프로그램 실행 시 사용자로부터 가로(width)와 세로(height) 값을 입력 받아 객체를 생성하고 area() 메서드를 호출하여 넓이를 출력



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


width = int(input("가로(width)를 입력하세요: "))
height = int(input("세로(height)를 입력하세요: "))

area_quad = Rectangle(width, height)

# 넓이 출력
print("사각형의 넓이:", area_quad.area())
'''


# 문제1. User 클래스 구현

class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"

    @classmethod
    def get_total_users(cls):
        return cls.total_users


user1 = User("홍길동")
user2 = User("김철수")

user1.add_points(100)
user2.add_points(450)

print(user1.username, user1.get_level())
print(user2.username, user2.get_level())

print("총 유저 수:", User.get_total_users())
