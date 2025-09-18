'''# 문제1. 구구단 만들기
import random
for num2 in range(2, 10):  # 2단부터 9단까지 반복
    print(f"[{num2} 단]")
    for i in range(1, 10):  # 각 단에서 1~9까지 곱하기
        print(f'{num2} x {i} = {num2 * i}')


# 문제2. 중첩 for문 별찍기

n = int(input('몇줄?: '))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

n = int(input('몇줄?: '))

for i in range(1, n+1):
    for j in range(n-i):
        print("", end='')

    for k in range(2 * i - 1):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print("", end='')
    # (i - 1) * 2 + 1 = 2i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()


n = int(input('몇줄?: '))

for i in range(1, n+1):
    print(' '*(n-i) + i * '*')


n = int(input('몇 줄 ? >'))

print('[왼쪽 정렬]')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    # (i - 1) * 2 + 1 = 2i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print('[오른쪽 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    for k in range(i):
        print('*', end='')
    print()


# 문제1. 제곱값 리스트 만들기
print([i ** 2 for i in range(1, 11)])


# 문제 2. 3의 배수만 리스트로 만들기
# ▪ 1부터 50까지의 수 중에서 3의 배수만 포함된 리스트를 리스트 컴프리헨션으로 만들어 출력하세요.

list = [i for i in range(1, 51) if i % 3 == 0]
print(list)


# 문제 3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
# ▪ 위 리스트에서 글자 수가 5 이상인 단어들만 리스트 컴프리헨션으로 추출하여 출력하세요.
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

print([i for i in fruits if len(i) >= 5])


# 문제1. 비밀 코드 맞추기(1)


secret_code = 'codingonre3'

while True:
    code = input("비밀 코드를 입력하세요: ")
    if code == secret_code:
        print("입장이 허용되었습니다!")
        break
    print('다시 입력하세요')


# 문제2. 업다운 게임

random_value = random.randrange(1, 101  # 한 번만 생성
n=0

while True:
    num=int(input('숫자를 입력하세요 (1~101): '))
    n += 1  # 입력할 때마다 시도 횟수 증가

    if num > random_value:
        print("입력한 숫자보다는 작아요.")
    elif num < random_value:
        print("입력한 숫자보다는 커요.")
    else:
        print(f"{n}번 만에 정답을 맞췄습니다!")
        break'''


# 문제2. 유효한 나이만 평균 내기


times = 0
sum_age = 0

while times < 5:
    age = int(input('나이를 입력하세요: '))

    if 0 <= age <= 120:
        sum_age += age
        times += 1

    else:
        print("나이를 다시 입력하세요")
else:
    avg = sum_age // 5
    print(f'"총합: "{sum_age}, "평균: " {avg}')
