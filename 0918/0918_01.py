# 함수(funcion)

# 함수는 특정 작업을 수행하는 코드의 묶음입니다.
# 한 번 정의하면 필요할 때마다 호출하여 재사용할 수 있습니다.

# 함수를 사용하는 이유
# 1. 코드 재사용성 : 같은 코드를 반복 작성할 필요 없음
# 2. 모듈화: 프로그램을 작은 단위로 나누어 관리
# 3. 가독성 향상: 코드의 의도를 명확히 표현
# 4. 유지보수 용이: 수정이 필요할 때 함수만 변경
# 추상화: 복잡한 로직을 단순한 인터페이스로 제공


print('=' * 20)
print('첫번째 섹션')
print('=' * 20)


# 함수 사용 - 코드 재사용
def print_section(title):
    print('=' * 20)
    print(f'{title} 섹션')
    print('=' * 20)


print_section('첫번째')


# 함수 정의와 호출
# 함수 정의(Defintion)
def 함수이름(매개변수):
    # 실행 코드
    return (반환값)

# 함수 호출 (call)
# 결과 = 함수이름(인자)


def say_hello():
    print('안녕하세요')


def greet(name):
    print(f'안녕하세요{name}님!')


greet('33')


def add(a, b):
    result = a + b
    return result


sum_result = add(3, 5)

# 사각형 넓이


def calculate_area(width, height):
    '''
    직사각형의 넓이를 계산

    parameters:
        width (float) : 직사각형의 너비
        height (float) : 직사각형의 높이 

    return:
        float : 직사각형의 넓이

    '''

    return width * height


print(calculate_area(10, 20))

# docsting 확인
print(calculate_area.__doc__)
help(calculate_area)


# 매개변수는 하나. 인자는 여러개 쓸 수 있게 해주는 위치 가변인자
# *

def add_all(*new_tuple):
    return sum(new_tuple)


result = add_all(1, 2, 3, 4, 5)


def print_info(**new_dic):
    for key, value in new_dic.items():
        print(f'{key}{value}')


print_info(name='홍길동', age=30, city='서울')


# 매개변수와 인자
# 매개변수(parameter): 함ㅁ수 정의시 사용하는 변수
# 인자(Argument) : 함수 호출시 전달하는 실제 값

def multiply(x, y):  # x,y는 매개변수
    return x*y


result = multiply(3, 5)  # 3,5는 인자

# 위치 인자(positional Arguments)


def introoduce(name, age, city):
    print(f'{name}{age}{city}')


# name = 김철수, age = 25, city = 서울
introoduce('김철수', 25, '서울')

# 키워드 인자 (keyword Arguments)


def introoduce(name, age, city):
    print(f"{name}{age}{city}")


# 순서와 상관없이 이름을 전달
introoduce(city='서울', age=25, name='김철수')

# 위치 인자, 키워드 혼용
introoduce('김철수', city='서울', age=25)

# 주의: 위치 인자는 키워드 인자보다 앞에 와야합니다.

# 반환값(return)
# 단일 값 반환


def square(n):
    return n ** 2


result = square(5)
print(result)  # 25

# 여러 값 반환


def calculate_stats(number):
    total = sum(number)
    avg = total/len(number)
    maxnum = max(number)
    minnum = min(number)

    return total, avg, maxnum, minnum


numbers = [100, 200, 300, 400]
a, b, c, d = calculate_stats(numbers)

print('total: ', a)
print('avg: ', b)
print('maxnum: ', c)
print('minnum: ', d)

state = calculate_stats(numbers)
print(state)  # (1000, 250.0, 400, 100)


# return의 특징
def check_positive(number):
    if number > 0:
        return "양수"
    elif number < 0:
        return "음수"
    else:
        return "0"

    print('이 코드는 실행 안됨')
# return 은 함수를 종료 시킨다.


# 조기 반환(early Return)

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다. "

    return a/b

# 기본값 매개변수


def greet(name, greeting="안녕하세요"):
    print(f'{greeting},{name}님')


greet('김철수')


# 여러 기본값
def create_profile(name, age=25, city='서울', job='개발자'):
    return {'name': name, 'age': age, 'city', city, job}
