'''# for문 기본 사용
# for문 : 정해진 횟수만큼 반복

for i in range(5):
    print('안녕하세요')

# range(끝) - 0부터 -1 까지
range(5)

# range(시작, 끝) - 0부터 -1 까지
range(2, 6)

# range(시작, 끝, 간격) - 0부터 -1 까지
range(2, 6, 2)


for i in range(5):
    print(f'i의 값 {i}')


# 구구단 전체

for num in range(1, 10):
    print(f'{num} 단')
    for i in range(1, 10):
        print(f'{num} x {i} = {num * i}')

# 과일 리스트 순회
fruits = ["사과", "바나나", "오렌지", "포도"]

for fruit in fruits:
    print(f'과일 : {fruit}')

scores = [65, 27, 87, 86]
for score in scores:
    print(f'점수 : {score}')

# 총점
total = 0

scores = [65, 27, 87, 86]
for score in scores:
    total += score
    print(f'점수 : {score}')

print("total : ", total)

# 평균
total = 0
count = 0

scores = [65, 27, 87, 86]
for score in scores:
    total += score
    print(f'점수 : {score}')

print("total : ", total)
print("avg : ", total / count)'''


#
word = "python"
# 나중에 추가 !


# 중첩 for 문 - 반복 속의 반복
# 별 패턴

for i in range(1, 6):
    print('*****')


for j in range(1, 6):
    for i in range(5):
        print()
