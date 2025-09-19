'''# 로그인/로그아웃 전역 상태 관리
# 전역 변수

current_user = None


def login(name):
    global current_user
    if current_user != None:
        print('이미 로그인 되어 있습니다')
    else:
        current_user = name
        print(f'{name}님 로그인 성공')


def logout():
    global current_user
    if current_user



# 4. 제곱
def sqa(a, b):
    if b == 0:
        return 1
    return a * sqa(a, b - 1)


print(sqa(2, 2))


# 1부터 n까지의 합
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)


print(sum_to_n(5))

# 문자열 뒤집기


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string('hello'))



print(sum_to_n(5))


# 5. 팩토리얼
# 반복문

def factorial_for(n):
    result = 1
    for i in range(1, n + 1):   # 1부터 n까지 반복
        result *= i
    return result


print(factorial_for(7))

# 재귀함수


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(7))

# 6. 피보나치 수열
# 반복문


# 재귀함수
def fibonacci(n):
    if n <= 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(10):
    print(fibonacci(i))

print()
'''

students = [("Alice", [80, 90]), ("Bob", [60, 65]), ("Charlie", [70, 70])

a+b/2 >= 70
