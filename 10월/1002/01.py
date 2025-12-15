import pandas as pd

# print(pd.__version__)

# 데이터 분석
# 과정
'''
데이터 수집 -> 데이터 정제 -> 데이터 탐색 -> 데이터 분석 -> 시각화 
-> 인사이트 도출
'''

# 데이터 수집
''' 분석할 자료를 모으는 단계 '''
# 데이터 정제
'''분석 가능한 형태로 만드는 단계'''
# 데이터 탐색
'''데이터의 특성을 파악하는 단계'''
# 데이터 분석
'''가설을 검증하고 패턴을 찾는 단계'''
# 시각화
'''결과를 이해하기 쉽게 표현하는 단계'''
# 인사이트 도출
'''분석 결과를 의사결정에 활용하는 단계'''

# Excel, pandas 비교
'''
Excel로 100만개 데이터를 처리한다면?
2019 버전 10000000행 까지만 제한
파일 열기만 해도 5분 이상 소요 , 수직 계싼 시 프로그램 멈춤
반복 작업을 매번 수동으로 해야함
'''

# Series
# Pandas의 가장 기본되는 1차원 데이터 구조
'''
1. 1차원 배열: 데이터가 일렬로 나열되어 있습니다.
2. 레이블(인덱스) 보유: 각 데이터에 이름표를 붙일 수 있습니다.
3. 동일 타입: 하나의 series 안의 모든 데이터는 같은 타입
'''

simple_series = pd.Series([10, 20, 30, 40, 50])
print(simple_series)

'''
Series = Value(값), Index(인덱스) + Name(이름)
'''

data_series = pd.Series(
    data=[10, 20, 30, 40, 50],
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    name='Test_Score'

)

'''
pd.Series(data= None, index=None, name = None)

매개변수 설명
data = None 실제 데이터(필수)
    -리스트, 딕셔너리, 스칼라값, Numpy 배열

Index = None 인덱스 레이블(선택)
    - 기본값 0, 1, 2---
    - 리스트, 배열 등으로 지정

dtype = None 데이터 타입(선택)
    -자동 추론되지만 명시 가능
    -
'''


'''
각 구성요소의 역할:
value(값)
    실제 데이터가 저장되는 부분
    numpy 배열로 저장됨
    빠른 수치 연산 가능
index(인덱스)
    각 값을 식별하는 레이블
    기본값: 0, 1, 2, ...(정수)
name(이름)
    Series 전체를 설명하는 이름
    선택사항(없어도 됨)
    DataFrame 결합 시 컬럼명이 됨
'''

int_series = pd.Series([1, 2, 3, 4, 5])
print(f'Integer SEres dtype:  {int_series}')

float_series = pd.Series([1.1, 2.1, 3.1, 4.1, 5.1])
print(f'Integer SEres dtype:  {float_series}')

str_series = pd.Series(['apple', 'banana'])
print(f'Integer SEres dtype:  {str_series}')

bool_series = pd.Series([True, False, True])
print(f'Integer SEres dtype:  {bool_series}')

mixed_series = pd.Series([1, 2.5, 3])
print(f'Mixed Series dtype: {bool_series}')

# dtype 이 중요한 이류
'''
메모리 사용량 결정
연산 가능 여부
성능에 영향 '''


int_series = pd.Series([1, 2, 3, 4, 5])
print(f'Integer SEres dtype:  {int_series}')


temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name='4월 기온')
print(temp)

date = pd.date_range('2025-04-01', periods=5)
print(date)

temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print(temp_date)

product = {
    '노트북': 15,
    '마우스': 40,
    '키보드': 20
}

product_series = pd.Series(product, name='현재 재고')
print(product_series)


scalar_series = pd.Series(0, index=['월', '화', '수', '목'], name='판매량')
print(scalar_series)


test_scores = pd.Series(
    data=[65, 85, 97, 86, 65],
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    name='Exam'
)

print("======속성 전체========")

# 1. value - 실제 데이터(Numpy 배열)
print('1. values(값들)')
print(test_scores.values)


print('2.  index(인덱스)')
print(test_scores.index)


# 인덱싱과 슬라이싱
# 인덱싱

# Series에서 특정 데이터를 선택하는 방법
# 위치 기반 0, 1, 2,
# 레이블 기반: 인덱스 이름으로 접근

sales = pd.Series([100, 200, 150, 300, ], index=['Mon', 'Tue', 'Wed', 'Thu'],
                  name="Daily_Sales")

wed_sales = sales['Wed']
print('수요일 매출1', wed_sales)

# wed_sales2 = sales[2]
# print('수요일 매출2', wed_sales2)
print('수요일 매출2', sales.iloc[2])

selected_days = sales[['Mon', 'Wed', 'Thu']]
print(selected_days)

# 슬라이싱
print('처음부터 수요일 포함')
print(sales.loc[:'Wed'])

# 처음부터 끝까지 
print(sales.iloc[:])
