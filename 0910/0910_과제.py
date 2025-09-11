
# 실습1. 영화 정보 출력하기

title = "Inception"
director = "Christopher Nolan"
year = 2010
genre = "Sci-Fi"

print(f"Title: {title} Director: {director} Year: {year} Genre: {genre}")


# 실습2. 자기소개 하기

name = "서주연"
age = 24
MBTI = "ESTJ"

print(f"안녕하세요\n제 이름은 {name}이고\n{age}살입니다.\n제 MBTI는 {MBTI}에요.")

print(f"""안녕하세요
제 이름은 {name}이고
{age}살입니다.
제 MBTI는 {MBTI}에요.""")


# 실습 3 대학생의 용돈관리
money = 300000
money -= 80000
money -= 9000*5
money += 120000
money *= 1.2
money *= 2/3

print(money)


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
