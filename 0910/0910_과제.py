# ========================================
# 실습 문제 1: 영화 정보 출력
# ========================================

# 영화 정보를 변수에 저장
title = "Inception"                    # 영화 제목
director = "Christopher Nolan"         # 감독명
year = 2010                           # 개봉연도
genre = "Sci-Fi"                      # 장르

# f-string을 사용하여 영화 정보 출력
print(f"영화 제목: {title}")
print(f"감독: {director}")
print(f"개봉연도: {year}")
print(f"장르: {genre}")

# 한 줄로 모든 정보 출력
print(f"Title: {title}, Director: {director}, Year: {year}, Genre: {genre}")

# ========================================
# 실습 문제 2: 자기소개 출력 (여러 줄 문자열)
# ========================================

# 개인 정보를 변수에 저장
person_name = "juyeon"                 # 이름
person_age = 24                      # 나이
person_mbti = "ESTJ"                  # MBTI 성격유형

# 여러 줄 문자열(""")과 f-string 조합 사용
introduction = f"""안녕하세요!
제 이름은 {person_name}이고,
{person_age}살입니다.
제 MBTI는 {person_mbti}예요.
만나서 반갑습니다!"""

print(introduction)

# 한 줄로도 출력 가능
print(f"안녕하세요! 제 이름은 {person_name}, {person_age}살, 제 MBTI는 {person_mbti}예요.")


# ========================================
# 실습 1: 가계부 프로그램 (복합 할당 연산자 활용)
# ========================================

print("\n=== 실습 1: 가계부 프로그램 ===")

# 초기 잔액 설정
money = 300000                  # 초기 잔액 30만원
print(f"초기 잔액: {money:,}원")

# 1. 생활용품 구매 (8만원 지출)
money -= 80000                  # money = money - 80000
print(f"생활용품 구매 후: {money:,}원")

# 2. 교통비 지출 (9,000원 × 5일 = 45,000원)
money -= 9000 * 5               # money = money - (9000 * 5)
print(f"교통비 지출 후: {money:,}원")

# 3. 알바비 수입 (12만원 입금)
money += 120000                 # money = money + 120000
print(f"알바비 입금 후: {money:,}원")

# 4. 적금 이자 (20% 이자 적용)
money *= 1.2                    # money = money * 1.2
print(f"적금 이자 적용 후: {money:,}원")

# 5. 생활비 지출 (현재 잔액의 1/3 사용)
money -= money / 3              # money = money - (money / 3)
print(f"생활비 지출 후: {money:,.0f}원")

"""
money -= money / 3 설명:
1. 현재 money 값을 3으로 나눔
2. 그 결과를 현재 money에서 뺌
3. 결과적으로 원래 금액의 2/3가 남게 됨

예: money가 300이면
money -= money / 3
money = money - (money / 3)
money = 300 - (300 / 3)
money = 300 - 100 = 200
"""

# EDM 리듬 트랙 만들기
intro = "둠칫"
drop = "두둠칫"

print(intro + drop * 3)


# input 연습하기

name = input("이름: ")
age = input("나이: ")

print(f"안녕하세요. 저는{name}이고, {age}살입니다.")


# 입력과 연산 연습하기
# 1. 넓이, 둘레

width = int(input("가로 길이를 입력하세요: "))
heigth = int(input("세로 길이를 입력하세요: "))

print(f"""넓이: {width*heigth} 
둘레: {width*2 + heigth*2} """)

# 2. 네 자릿수 정수 입력, 각 자릿수를 분리

num = input("네 자릿수 정수를 입력하세요: ")

print(f"""천의 자리: {num[0]}
백의 자리: {num[1]}
십의 자리: {num[2]}
일의 자리: {num[3]}""")


# 발표 순서와 발표 주제 정하기
name1, name2, name3 = input("발표자 이름 3명을 입력하세요: ") .split()
sub1, sub2, sub3 = input("발표 주제 3개를 입력하세요: ") .split()

print(f""" 발표 순서 안내입니다.
1조 발표자: {name1}  - 주제: {sub1}
2조 발표자: {name2}  - 주제: {sub2}
3조 발표자: {name3} - 주제: {sub3}""")


# 날짜와 시간
# 년, 월, 일과 시, 분, 초를 한번에 입력 받아서 출력하기

year, month, day = input("년.월.일을 입력하세요: ") .split(".")
hour, minute, second = input("시:분:초를 입력하세요: ") .split(":")
print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
시작 시간은 {hour}시 {minute}분 {second}초입니다. """)
