# 비교 연산자
x = 10
y = 20

print(f'x == y : {x == y}')
print(f'x != y : {x != y}')
print(f'x >= y : {x >= y}')
print(f'x > y : {x > y}')
print(f'x <= y : {x <= y}')
print(f'x < y : {x < y}')

# 논리 연산자
print(True and False)
print(True and True)
print(False and True)
print(False and False)

# ctrl + D 찾기 연산자?

print(True or False)
print(True or True)
print(False or True)
print(False or False)


print(f' not True : {not True}')
print(f' not False : {not False}')

print(True and False or True)
print(True and (False or True) and False)

# 조건문 기본 문법
a = 10
if a == 10:
    print(f'a: {a}')

'''
들여쓰기 안 내용(코드블록)은 if 문의 조건에 만족해야 실행됨
코드 블록이 없는 경우 : pass 사용
'''

age = 20
if age >= 18:
    print("성인입니다")

# if-else

# if -elif - else
name = '철수'

if name == '김철수':
    print(f'김철수 입니다')
elif name == '철수':
    print(f'철수입니다')
else:
    print('이름을 입력하세요')


# 중첩 조건문
