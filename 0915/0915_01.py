# Tuple
# 순서가 있는 불변 시퀀스 자료 구조
# 한 번 생성되면 수정할 수 없는 리스트와 유사한 구조
# 여러 개의 값을 하나의 단위로 묶을 때 사용

# 왜 Tuple이 필요한가?
# 변경되면 안되는 데이터 보호
# 리스트 사용시 -> 실수로 변경 가능
'''
coordinates_list = [37.345, 126.432] # 특정 좌표 
coordinates_list[0] = 0 # 실수로 변경 가능

# 튜플 사용시 -> 변경 불가능

coordinates_list = (37.345, 126.432) # 특정 좌표 
coordinates_list[0] = 0 # typeError! 발생 변경 불가능 
'''
# 특징
# 불변성 : 생성 후 수정 불가능
# 순서 보장 : 인덱스로 접근 가능
# 중복 허용 : 같은 값 여러 번 저장 가능
# 해시 기능 : 딕셔너리 키로 사용 가능
# 메모리 효율적 : 리스트보다 적은 메모리 사용

# 1. 소괄호 사용
empty_tuple = ()
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
print(mixed)

# 2. 소괄호 없이 생성
numbers2 = 1, 2, 3, 4, 5
print(type(numbers2))

# 3. tuple()생성자 사용
from_list = tuple([1, 2, 3, 4])
print('type(from_list) : ', type(from_list))

from_str = tuple("hello")

print(type(from_str))

# 4. 단일 요소 튜플 ( , 필수 !!)
single = (10,)
print(type(single))

not_tuple = (10)
print(type(not_tuple))

# 5. range 튜플 생성
range_tuple = tuple(range(1, 10))
print('type(range_tuple): ', type(range_tuple))
print(range_tuple)


# tuple 접근과 슬라이싱
fruits = ('사과', '바나나', '수박', '오렌지', '포도')

print(fruits[1])  # 바나나
print(fruits[-1])  # 포도
print(fruits[::-1])

# 슬라이싱으로 새 튜플 생성
first_three = fruits[0:2]
last_two = fruits[-2:]

# 처음 3개랑, 마지막 두개
combined = first_three + last_two


# 불변성 확인
numbers = (1, 2, 3, 4, 5, 6)

# 수정 시도 - 모두 에러 발생
# numbers[0] = 10 # typeError
# numbers.append(6)
# del numbers[1]

# 하지만 새 튜플 생성은 가능
'''new_numbers = numbers + (1, 2)
tuple_whit_list[0].append(3)
print('')
'''
#  언패킹(unpacking)
coordinates = (10, 20)
x, y = coordinates
print(f'x : {x}, y: {y}')

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print('first', first)
print(middle)

# 빈 리스트 생성
first, *rest = (1,)
print('first', first)
print('rest', rest)

# tuple 메서드
numbers = (1, 1, 3, 3, 2, 2, 5, 3, 4)

# count() - 특정 값의 개수
count_2 = numbers.count(2)
print('count_2', count_2)

# index() - 특정 값의 인덱스
# 없는 값 검색 시 에러
index_4 = numbers.index(4)


# 안전한 검색
value = 10
if value in numbers:
    print(f'{value}의 인덱스: {numbers.index(value)}')
else:
    print(f'{value}는 튜플에 없습니다. ')


tuple1 = (1, 2, 3)
tuple2 = (5, 6, 7)

# 연산

# 곱셈(반복)

# 비교 연산 (사전식 비교 _ 앞에서부터 비교)
print(tuple1 < tuple2)

# 길이, 최대, 최소, 합
numbers = (1, 2, 3, 4)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
