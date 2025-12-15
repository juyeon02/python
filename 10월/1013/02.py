import pandas as pd
import numpy as np

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}

df = pd.DataFrame(data)

# 인덱싱
print('===인덱싱===')
print(df[['이름', '직업']])

# 슬라이싱
print(df[1:3])
print(df[-2:])

# DataFrame의 슬라이싱은 행(row)기준으로 동작한다.
# 열 단위 슬라이싱은 명시적으로 지정
print(df[-2:]['이름'])

# iloc
print(df.iloc[0])  # 0번 행 전체
print(df.iloc[:, 1])  # 모든 행의 1번 (컬럼) 나이

# 결측값(Missing Value)
# 비어있는, 알 수 엇는, 기록되지 않은 데이터

# 종륲

missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})

# 결측값 탐지
# isnull() / isna()
# 결측값이면 True

# notna() / notnull()
# 값이 있으면 True

# 결측값 처리 전략
'''
삭제 - 결측값이 있는 행 / 열 제거
대체 - 다른 값으로 채우기
예측 - 앞뒤 값이나 패턴으로 추정
'''

# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})

# 삭제
drop_rows = sales_data.dropna()
print('결측값이 있는 행 삭제: ')
print(drop_rows)

# 결측값이 있는 열 전체 삭제
drop_cols = sales_data.dropna(axis=1)
print('결측값이 있는 열 삭제: ')
print(drop_cols)

# 특정 열 기준 삭제
drop_sales = sales_data.dropna(subset=['sales'])
print('sales 열 기준으로 삭제: ')
print(drop_sales)

# 대체
fill_mean = sales_data.copy()
fill_mean['sales'] = fill_mean['sales'].fillna(fill_mean['sales'].mean())
print(fill_mean)

# 시계열 대체
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채운다.

fill_forward = sales_data.copy()
fill_forward['sales'] = fill_forward['sales'].fillna(method='ffiill')
print(fill_forward)

# Backward Fill(뒤의 값으로 채우기)

fill_backwqrd = sales_data.copy()
fill_backwqrd