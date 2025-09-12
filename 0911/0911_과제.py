# 날씨에 따른 준비물 안내
'''
weather = input("오늘의 날씨는? : ")

if weather == "비":
    print("우산을 챙기세요!")

if weather == "맑음":
    print("선크림을 바르세요!")
'''

# 짝수 홀수 판별하기

'''num = int(input("정수를 입력해 주세요: "))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")'''

# 나이에 따른 영화 관람 가능 여부
'''
age = int(input('나이를 입력하세요: '))
if age <= 12:
    print("전체 관람가")
elif age <= 15:
    print('12세 이상 관람가')
elif age <= 18:
    print('15세 이상 관람가')
else:
    print("청소년 관람불가 가능")'''

# 시,분,초 구하기

'''time = int(input("초를 입력하세요: "))

hour = time // 3600
minute = time % 3600 // 60
second = time % 60

if time / 60 < 1:
    print(f"{time}초")
elif time / 60 >= 1 and time < 3600:
    print(f"{minute}분 {second}초")
else:
    print(f"{hour}시간 {minute}분 {second}초")'''

# 시-> 분-> 초 순으로 하면 and 안 써도 됨 ㅎㅎ^^^


# 중첩 조건문 (NEsted if)

김밥 = 2500
삼각김밥 = 1500
도시락 = 4000

money = int(input("금액을 입력하세요 : "))
food = input('식품명을 입력하세요 ( 김밥/삼각김밥/도시락): ')

if food == '김밥':
    if money >= 김밥:
        print("구매되었습니다.")
    else:
        print("금액이 부족합니다.")

elif food == '삼각김밥':
    if money >= 삼각김밥:
        print("구매되었습니다.")
    else:
        print("금액이 부족합니다.")

elif food == '도시락':
    if money >= 도시락:
        print("구매되었습니다.")
    else:
        print("금액이 부족합니다.")

# 구구단 만들기 _ 4단
print('4단')
for i in range(1, 10):
    print(f' 4 x {i} = {4*i}')
