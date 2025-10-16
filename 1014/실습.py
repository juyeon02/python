import pandas as pd
import numpy as np
'''
df = pd.DataFrame({
    '이름': ['민준', '서연', '지후', '서준', '지민'],
    '점수': [78, 92, 85, 60, 88],
    '반': [1, 2, 1, 2, 1]
})


# 1. 점수(score)가 80점 이상인 학생만 추출하세요.
df1 = df[df['점수'] >= 80]
print(df1)
print()

# 2. 1반(반==1) 학생들 중, 점수가 85점 이상인 학생만 추출하세요.
df2 = df[(df['반'] == 1) & (df['점수'] >= 85)]
print(df2)
print()

# 3. 이름이 '서연' 또는 '지민'인 학생만 추출하세요.
df3 = df[df['이름'].isin(['서연', '지민'])]
print(df3)
print()

# 4. 문제 3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력하세요.
df4 = df3.reset_index(drop=True)
print(df4)
print()

# 5. 점수가 80점 미만이거나 2반인 학생만 추출하세요.
df5 = df[(df['반'] == 2) | (df['점수'] < 80)]
print(df5)
print()

# 6. 문제 5의 결과에서 '점수' 컬럼이 70점 이상인 학생만 다시 추출하고, 인덱스를 재정렬하여 출력하세요
df5 = df5[df5['점수'] >= 70]
df6 = df5.reset_index(drop=True)
print(df6)



df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '국어': [90, 80, 70]
})
# 1. '수학' 점수 [95, 100, 88]을 새 열로 추가하세요.
df['수학'] = [95, 100, 88]
print(df)
# 2. 1번 문제의 DataFrame에서 '이름' 열을 삭제하세요.
print(df.drop('이름', axis=1))

print()


df = pd.DataFrame({
    '제품': ['A', 'B'],
    '가격': [1000, 2000]
})

# 3. 제품 'C', 가격 1500인 새 행을 추가하세요.

# 방법 1
df3 = pd.DataFrame([{
    '제품': 'c',
    '가격': 1500
}])

df = pd.concat([df, df3], ignore_index=True)
print(df)


# 방법 2
df.loc[len(df)] = ['D', 2500]
print(df)


# 4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
print(df.drop(0))

print()

df = pd.DataFrame({
    '과목': ['국어', '영어', '수학'],
    '점수': [85, 90, 78]
})

# 5. '점수'가 80 미만인 행을 모두 삭제하세요.
# 방법 1
df5 = df[df['점수'] >= 80]
print(df5)


# 방법 2
df = df.drop(df[df['점수'] < 80].index)
print(df)

# 6. '학년' 열(값은 모두 1)을 추가하세요
df['학년'] = 1
print(df)


df = pd.DataFrame({
    '이름': ['A', 'B'],
    '나이': [20, 22]
})
# 7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
#  (단, '키'라는 새 열이 자동으로 추가되어야 함)
df7 = pd.DataFrame([{'이름': 'c', '나이': 25, '키': np.nan}])
df = pd.concat([df, df7], ignore_index=True)
print(df)
print()


df = pd.DataFrame({
    '부서': ['영업', '기획', '개발', '디자인'],
    '인원': [3, 2, 5, 1]
})

# 8. 인원이 2명 이하인 행을 모두 삭제하고
# 방법 1
df = df[df['인원'] > 2]
print(df)

# 방법 2
df = df.drop(df[df['인원'] <= 2].index)
print(df)

# 9. '평가' 열을 새로 추가해 모든 값을 '미정'으로 채우세요.
df['평가'] = '미정'
# 그냥 값 전체 지정! , [] 로 할거면 갯수가 동일해야 함.
print(df)


df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [88, 95, 70, 100]
})
# 1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
df_score = df.sort_values(by='score')
print(df_score)

# 2. score 컬럼 기준 내림차순으로 정렬한 후, 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를출력하세요.
df_score = df.sort_values(by='score', ascending=False)
print(df_score)
df_score_index = df_score.sort_index(ignore_index=False)
print(df_score_index)


# print(df.sort_values(by = 'score), ascending=False,).reset_index

df = pd.DataFrame({
    '이름': ['가', '나', '다', '라', '마'],
    '반': [2, 1, 1, 2, 1],
    '점수': [90, 85, 80, 95, 85]
})
# 3. 주어진 DataFrame에서,반(class) 기준 오름차순, 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결과를 출력하세요.
df_sorted = df.sort_values(by=['반', '점수'], ascending=[True, False])
print(df_sorted)

# 4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
df_col = df.sort_index(axis=1)
print(df_col)


df = pd.DataFrame({
    'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])
# 5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
df_index = df.sort_index()
print(df_index)

# 6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하세요.
df_index = df.sort_index(ascending=False)
print(df_index)

df = df.sort_values(by='value')
print(df)
'''

# 실습4. groupby 연습문제(1)

df = pd.DataFrame({
    'grade': [1, 2, 1, 2, 1, 3],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
    'kor': [85, 78, 90, 92, 80, 75]
})

# 1. 각 학년(grade)별 평균 국어 점수(kor)를 구하세요.
print('1')
print(df.groupby('grade')['kor'].mean())

df = pd.DataFrame({
    'class': [1, 1, 1, 2, 2, 2],
    'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
    'score': [80, 90, 85, 70, 95, 90]
})

# 2. 반(class)별, 과목(subject)별로
# 시험에 응시한 학생 수(count)와 평균 점수(avg)를 구하세요.
print('2')

result = df.groupby(['class', 'subject'])['score'].agg(['count', 'mean'])
print(result)

df = pd.DataFrame({
    'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu'],
    'seller': ['A', 'B', 'A', 'B', 'A'],
    'sales': [100, 200, 150, 120, 130]
})

# 3.지역(region)별 판매자(seller)별로
# 판매액(sales)의 합계와 최대값을 구하세요.

print(df.groupby('region')['sales'].sum())
print(df.groupby('region')['sales'].max())


print(df.groupby('seller')['sales'].sum())
print(df.groupby('seller')['sales'].max())


df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'A', 'B'],
    'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
    'score': [3, 2, None, 1, 4, 2]
})

# 4. 팀(team)별, 포지션(position)별로
# 결측치(NaN)를 포함한 점수(score)의 평균을 구하세요.

print(df.groupby(['team', 'position'], dropna=False)['score'].mean())

# dropna=False 결측치 포함!!! 


df = pd.DataFrame({
    'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
    'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})
# 5. 부서(dept)별로 성별(gender)별 인원 수와, 총 연봉(salary) 합계를 구하세요.
print(df.groupby(['dept', 'gender'])['salary'].agg(['count', 'sum']))


#방법 2
result = df.groupby(['deppt', 'gender']).agg(
    count = ('salary', 'count'), 
    total_salary = ('salary', 'sum')
)
