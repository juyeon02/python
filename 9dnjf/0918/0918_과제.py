# 문제1. 사칙연산 계산기 함수 만들기
def calculate(a, b, operator):
    result = 0

    if "+" == operator:
        result = (a + b)

    elif "-" == operator:
        result = (a - b)

    elif "*" == operator:
        result = (a * b)

    elif "/" == operator:
        result = (a / b)

    else:
        result = ("지원하지 않는 연산입니다")

    return result


print(calculate(1, 2, "+"))


# *args 사용 연습
# 문제 1. 숫자 여러 개의 평균 구하기

def average(*args):

    ave = sum(args)/len(args)
    return ave


print(average(1, 2, 3))


# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
# max : 자료의 범위 내에서 최대값을 구함
def text(*nnn):
    max_len = max(nnn)
    print(max_len)
    return


text('abd', 'addsf', 'asdfsdfsd')


# kwargs 사용 연습
# 문제 3. 사용자 정보 출력 함수

def information(**inf):
    for key, value in inf.items():
        print(f'{key}{value}')


information(name="홍길동", age=300, email="gildong@ddd.dd")


# 문제 4. 할인 계산기
# 상품 가격 목록을 **kwargs로 받아, 각각 10%씩 할인된 가격을 출력하는 함수를 작성하세요.
def price_list(**list):

    for key, value in list.items():
        print(f'{key}{value * 0.9}')


price_list(사과=2000, 바나나=2000)
