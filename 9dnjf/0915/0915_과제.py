# ====================================
#  실습1. 튜플 종합 연습
# ====================================

# step 1 손상된 고객 정보 복원하기
user = ("minji", 25, "Seoul")

restored_user = ('eunji',) + user[1:]   # ('eunji', 25, 'Seoul')
print(restored_user)

# Step 2. 고객 정보 언패킹하여 변수에 저장

name, age, city = ('eunji', 25, 'Seoul')

# Step 3. 지역별 보안 정책 분기 처리

if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

# Step 4. 고객 데이터 통계 분석

users = ("minji", "eunji", "soojin", "minji", "minji")

user_name = users.count("minji")
print('minji : ', user_name)

user_soojin = users.index('soojin')
print('soojin', user_soojin)

# Step 5. 고객 이름 정렬

sorted_users = sorted(users)
print(sorted_users)


# ====================================
#  실습2. set 종합 연습
# ====================================

# 문제 1. 중복 제거 및 개수 세기


submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
students = set(submissions)

print('제출한 학생 수 :', len(students))
print('제출자 명단 : ', students)

# 문제 2. 공통 관심사 찾기

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

print('공통 관심 장르 : ', user1 & user2)
print('서로 다른 장르: ', user1 ^ user2)
print('전체 장르: ', user1 | user2)


# 문제 3. 부분집합 관계 판단
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

print('지원 자격 충족 여부 : ', job_required.issubset(my_certificates))
