'''def add(a, b):
    a += 1
    return a + b


x = 10


def change_x():
    x = x + 5
    print(x)


change_x()


def outer():
    a = 10

    def inner():
        nonlocal a
        a += 5
        print(f"[inner] a: {a}")
    inner()
    print(f"[outer] a: {a}")


outer()
'''

# 변수의 범위란?
# 변수가 살아있는 (접근 가능한) 영역을 범위(scope)라고 합니다.
# 집= 전역범위
# 방 = 지역범위
# 방 안의 물건은 그 방에서만 사용 가능
# 거실의 물건은 모든 방에서 사용 가능


'''# 전역 변수(global variable)
global_var = '전역 변수'


def my_fun():
    # 지역 변수(local VAriable)
    local_var = '지역 변수'

    print(global_var)  # 전역 변수 접근 가능
    print(local_var)  # 지역 변수 접근 가능


my_fun()
print(global_var)  # 전역 변수 접근 가능
# print(local_var) # 에러! 함수 밖에서 지역 변수 접근 불가능

# global 키워드
# 함수 안에서 전역 변수를 수정하려면 global 키워드를 사용합니다.

count = 0

# def increment_wrong():
    # count = count + 1 # 에러


def increment_right():
    global count
    count = count + 1


score = 0 

def add_Score(point):
    glo


def calculate_average(numbers):
    if not numbers:      #  빈 리스트면 출력
        return 0 
    return sum(numbers) / len(numbers)

def num_append(numbers):
    numbers.append(6)

numbers = [1, 2, 3, 4, 5]
num  = 10 
print('함수 호출 전 ' )

print


info_dic = {'name': '김철수'}


def change_info(info):
    info['name'] = '이영희'
    info['age'] = 25


print(numbers)


# 재귀함수 (recursive Function)

# 재귀함수는 자기 자신을 호출하는 함수

# 팩토리얼 계산 (n! = n X (n-1) X ...)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


# 피보나치 수열
# 0 1 2 3 5 8 13 ...

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(10):
    print(fibonacci(i))

print()
'''
# 람다 함수(Lamda function)
# 람다 함수는 이름 없는 한 줄까지 간단한 함수 입니다.


# 일반 함수
def square(x):
    return x ** 2


# 람다 함수 (같은 기능)
def square_lamda(x): return x ** 2


print((lambda x: x ** 2)(5))


# 여러 매개변수
def add(x, y): return x + y


numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# sorted() 정렬 기준 지정
student = [
    {'name': '홍길동', 'score: ': 80},
    {'name': '김철수', 'score: ': 92},
    {'name': '이영희', 'score: ': 72}
]
