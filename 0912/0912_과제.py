'''# 과제 1 실습. 인덱싱, 슬라이싱 복습문제
# 문제 1
nums = [10, 20, 30, 40, 50]
print('문제1: ', nums[0], nums[4])

# 문제 2
nums = [100, 200, 300, 400, 500, 600, 700]
print('문제2: ', nums[2:5])


# =======================
mid = 7 // 2
print(nums[mid-1:mid+2])
# ========================

# 문제 3. 리스트의 원소 두배 하기
nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2

print('문제3: ', nums)

# 문제4 리스트 뒤집기
items = ["a", "b", "c", "d", "e"]
print('문제4: ', items[::-1])

# 문제5 짝수 인덱스 요소만 출력
data = ["zero", "one", "two", "three", "four", "five"]
print('문제5: ', data[::2])

# 문제 6. 슬라이싱으로 리스트 수정하기

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = "매트릭스", "타이타닉"
print('문제6: ', movies)

# 문제 7. 특정 규칙에 따라 요소 추출
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
print('문제7: ', subjects[3::2])


# 문제 8. 리스트를 3개 구간으로 나누어 역순 병합

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data1 = data[0:3]
data2 = data[3:6]
data3 = data[6:]

print('문제8: ', data1[::-1], data2[::-1], data3[::-1])

# 실습 2
# 문제 1. 부분 삭제 후 연결

fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print('문제1: ', fruits)

# 문제 2. 반복 리스트 내부 요소 삭제
letters = ["A", "B"]
letters = letters * 3
del letters[2]
print('문제2: ', letters)
'''

# 실습 3
# 문제 1 기차 탑승 시뮬레이션

passenger = ["철수", "영희"]  # 철수 영희
passenger.extend(["민수", "지훈"])  # 철수 영희 민수 지훈
passenger.remove("영희")  # 철수 민수 지훈
passenger.insert(1, "수진")  # 철수 수진 민수 지훈
passenger.remove("민수")  # 철수 수진 지훈
passenger.reverse()
print('문제 1: ', passenger)  # 지훈 수진 철수

print()

# 문제 2. 숫자 처리 게임

list = [5, 3, 7]
list.extend([4, 9])  # 5, 3, 7, 4, 9
print(max(list))  # 9
print(min(list))  # 3
print(sum(list))  # 28
list.sort()
list.pop()
print(list)
