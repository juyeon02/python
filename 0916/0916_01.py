# Dictionary(딕셔너리)
# key-Value 쌍으로 데이터를 저장하는 자료구조
# 해시 테이블 기반으로 매우 빠른 검색 속도
# python의 가장 강력하고 유용한 자료구조 중 하나

student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾으려면?
target_id = "20230002"
if target_id in student_ids:
    index = student_ids.index(target_id)  # 0(n)
    name = student_names[index]
    print(name)

# 딕셔너리를 사용하는 경우 - 직관적이고 빠름
students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}

print(students["20230002"])  # 0(1) -  즉시 접근!

# 특징
# key-value 쌍:  각 값에 고유한 키로 접근
# 빠른 검색 : 0(1) 시간 복잡도
# 변경 가능(Mutable) : 요소 추가, 수정, 삭제 가능
# key는 유일 : 중복 키 불가(값은 중복 가능)
# 순서 보장 : python3.7+ 부터 삽입 순서 유지

# Dictionary 생성
# 1. 빈 딕셔너리 생성
empty_dict = {}  # dict
print(type(empty_dict))

# 2. 값이 있는 딕셔너리 생성
person = {
    'name': '김철수',
    'age': 25,
    'city': 'seoul'
}

print(person)

# 3. dict() 생성자 사용
person2 = dict(name='이영희', age=25, city='부산')
print('person2', person2)

# 4. 리스트/ 튜플로부터 생성
pairs = [('a', 1), ('b', 2)]
dict_from_pairs = dict(pairs)
print('dict_from_pairs', dict_from_pairs)

# 5. zip() 를 이용한 생성
keys = ['name', 'age', 'city']
values = ['박민수', '21', '대전']

person3 = dict(zip(keys, values))
print(person3)

# 6. dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print('squares', squares)

# 7. fromkeys() 메서드
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 1)
print('default_dict', default_dict)


# key 사용 가능한 타입
# hashable 타입만 key로 사용 가능
valid_dict = {
    1: "정수",
    3.14: "실수",
    '문자열': 'string',
    (1, 2): '튜플',
    True: '불리언',
    frozenset([1, 2]): "frozenset"
}

# UnHashable 타입은 key로 사용 불가
# 리스트 []
# set {1,2}
# 딕셔너리 : {'a' : 1}

# 접근과 수정
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터 공학',
    'gpa': 3.7
}

# 1. 대괄호 표기법 (keyError 위험)
name = student['name']
print('name', name)

# grade = student['grade']
# 에러

# get() 메서드(안전한 접근)
major = student.get('major')
print('magor', major)
grade1 = student.get('grade')
print('grade', grade1)

grade2 = student.get('grade', 'N/A')
print('grade', grade2)

# 기본값 지정
print('student.keys', student.keys)
print('student.items', student.items)
print('student.values', student.values)


student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}

# 값 수정, 추가
student['age'] = 23
print('student', student)

student['grade'] = 3
print('student', student)

# update( ) 메서드로 여러 값 한번에

student.update({
    'gpa': 4.0,
    'city': 'seoul',

})
print(student)

info_dict = {
    'age': 22,
    'grade': 1,
    'phone': '010-1234-1234'
}


student.update(info_dict)
print(student)

# 값 삭제
# del 키워드
del student['grade']
print('student', student)

# pop() 메서드 - 값은 반환하면서 삭제
popped = student.pop('phone')

# popitem() - 마지막 항목 제거
last_item = student.popitem()

student.clear()
# 안에있는 요소 모두 삭제
print('student', student)
