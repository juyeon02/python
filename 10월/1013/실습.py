import pandas as pd
import numpy as np

'''
# 다음 데이터를 CSV로 저장하고 다시 읽어오세요
practice_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

practice_data.to_csv('practice_data.csv', index=False)
pra_csv = pd.read_csv('practice_data.csv')
print(pra_csv)


# 한글 데이터를 UTF-8로 저장하고 읽어오세요
korean_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '직급': ['사원', '대리', '과장']
})

korean_data.to_csv('korean_data.csv', index=False, encoding='utf-8')
ko_csv = pd.read_csv('korean_data.csv', encoding='utf-8')
print(ko_csv)
'''

# 실습

data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)
# 1. ‘미세먼지’ 컬럼의 평균과 중앙값을 구하세요.
print('미세먼지 평균', df['미세먼지'].mean())
print('미세먼지 중앙값', df['미세먼지'].median())

# 2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요.
print('초미세먼지 최댓값', df['초미세먼지'].max())
print('초미세먼지 최솟값', df['초미세먼지'].min())

# 3. 각 컬럼별 결측값 개수를 구하세요.
print(df.isnull().sum())

print()
# 4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
df4 = df.dropna()
print(df4)
print('초미세먼지 평균', df4['초미세먼지'].mean())

# 5. 결측값을 모두 0으로 채운 뒤, # ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
df5 = df.fillna(0)
print(df5)
print('미세먼지 합계', df5['미세먼지'].sum())
print('초미세먼지 합계', df5['초미세먼지'].sum())

# 6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
fill_df = df.copy()
fill_df['미세먼지'] = fill_df['미세먼지'].fillna(fill_df['미세먼지'].mean())
print(fill_df)
print('미세먼지 표준편차', fill_df['미세먼지'].std())
