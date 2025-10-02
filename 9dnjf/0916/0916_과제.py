'''# 실습1. 딕셔너리
# 문제 1. 딕셔너리 핵심 개념 통합 실습

user = {}  # 1단계 빈 딕셔너리

user = {                            # 2단계: 사용자 기본 정보 추가
    "username": "skywalker",
    "email": "sky@example.com",
    "level": 5
}

email_value = user["email"]
print(email_value)

user["level"] = 6

print(user.get("phone", "미입력"))

user.update({"nickname": "sky"})
del user["email"]

user.setdefault("signup_date", "2025-07-10")
print('user', user)


# 문제 2. 학생 점수 관리
students = {}

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}

students["David"] = 80
students["Alice"] = 88

del students["Bob"]

print('students', students)




# 문제1. 리스트의 값을 두 배로 변환하기
numbers = [3, 6, 1, 8, 4]

num = []
for i in numbers:
    num.append(i*2)

print(num)


# 문제2. 문자열의 길이 구해서 새 리스트 만들기
words = ["apple", "banana", "kiwi", "grape"]

list = []
for i in words:
    list.append(len(i))
print(list)


# 문제3. 좌표 튜플에서 x, y 좌표 나누기
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print(f'x : {x_values}, y: {y_values}')
'''


# 문제1. 입력 받은 수의 합 구하기
n = int(input('숫자를 입력하세요:'))

num1 = 0
for i in range(1, n+1):
    num1 += i

print(num1)

# 문제2. 구구단 만들기
for num2 in range(1, 10):  # 1단부터 9단까지 반복
    print(f"{num2} 단")
    for i in range(1, 10):  # 각 단에서 1~9까지 곱하기
        print(f'{num2} * {i} = {num2 * i}')


# 문제3. 3의 배수의 합 구하기
# ▪ for 문과 range()를 사용하여 1부터 100까지의 수 중 3의 배수만 골라 합을 구해 출력하세요.
num3 = []
for i in range(1, 100):
    if i % 3 == 0:
        num3.append(i)

print(sum(num3))

# 문제4. 짝수이면서 5의 배수인 수 출력하기
n = int(input('숫자를 입력하세요:'))

num4 = []
for i in range(1, n+1, 2):
    if i % 5 == 0:
        num4.append(i)
print(num4)
