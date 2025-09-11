
# 변수 (varibale) - 데이터를 담는 상자

'''
상자(변수)에 물건(데이터)을 넣습니다
이름표(변수명)으로 상자를 구분
필요할 때 상자에서 물건을 꺼내 쓴다'''

# 변수 선언
# 변수 이름 = 값
age = 20
name = "김철수"
height = 175.5

# = -> 할당 연산자(넣는다는 의미, 수학의 등호와는 다름)
# 변수의 값은 바꿀 수 있다.

# 재할당
age = 30
print(age)


# 스네이크 케이스(snake_case)
student_name = "김철수"
user_age = 25
total_score = 100


x = 10
y = 20

# 값의 교환, 여러 변수 할당
x, y = y, x
# x,y = 20,10

X, Y = 30, "a"
# sep = 여러값 구분자 , end = '줄바꿈 구분자'
print(x, y, sep='  ', end='   ')
print(X, Y)

# 자료형
# 정수, 실수, 문자, 문자열
# 정수 => 2, 3, 12, 25
# 실수 => 1.1, 2.35
# 문자 => 'a', 'b'
# 문자열 => "aaa" , "bbb"

print('"파이썬"은 널리 사용되는 프로그래밍 언어 입니다.')

true = True
false = False

print('true', type(true))
print('false', type(false))


a = "1"
b = '1'

'''
a1 = int(a)
b1 = float(b)

print(type(a))
print('b type:', type(b1))
print('a type:', type(a1))
'''

# str() 문자열로 변환

c = 2
d = 2.1
# 문자열 포매팅 : f - string
print(f'c의 숫자는 {c} {d}입니다')


print(x, y, end='   ')
print(X, Y)
