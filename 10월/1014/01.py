import pandas as pd
import numpy as np

# 그룹화와 집계

# GroupBy
'''
그룹화는 데이터를 특정 기준에 따라 묶어서 분석하는 것 

전체 평균만으로는 부족한 경우 많음
카테고리별, 기간별로 나누어 보면 숨겨진 패턴 발견
세그먼트별 비교 분석 가능
'''

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

print('전체 직원 데이터')
print(employee_data)

# 전체 분석 vs 그룹별 분석
print('전체 분석')
overall_avg = employee_data['salary'].mean()
print(f'전체 평균 연봉 : {overall_avg}')

print('그룹별 분석')
dept_avg = employee_data.groupby('department')['salary'].mean()
print(dept_avg)

# GroupBy 핵심
'''
Split - Apply - Combine 
3단계 프로세스 

1. Split(분할) - 데이터를 그룹으로 나누기
2. Apply(적용) - 각 그룹에 함수 적용
3. combine(결합) - 결과를 하나로 합치기
'''
print('==========')
simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})

print('원본 데이터')
print(simple_data)

# 1단계 Split(분할)
for category, group in simple_data.groupby('category'):
    print(f'{category}그룹')
    print('group')

for category, group in simple_data.groupby('category'):
    avg = group['value'].mean()
    print(f'{category} 그룹 평균 {avg}')

result = simple_data.groupby('category')['value'].mean()
print(result)

# groupby(by=None, axis = 0, Leverl = None, as_index=True, sort = True...)
'''
by : 그룹화 기준(컬럼명 또는 컬럼명 리스트)
as_index : 그룹 키를 인덱스로 사용여부( 기본 = True)
sort: 그룹 키를 정렬할지 여부 (기본 = True)
'''

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

# 방법1 - 컬럼명 문자열
result1 = employee_data.groupby('department')['salary'].mean()
print(result1)

# 방법 2 - 컬럼 접근 후 집계
result2 = employee_data.groupby('department').salary.mean()
print(result2)

# 여러 컬럼 선택
result3 = employee_data.groupby('department')[['salary', 'years']].mean()
print(result3)

# as_index 매개변수
# 데이터 타입: 시리즈
result_indexed = employee_data.groupby('department', as_index=True)['salary'].mean()
print(result_indexed)


# 데이터 타입 : 데이터프레임
result_indexed = employee_data.groupby('department', as_index=False)['salary'].mean()
print(result_indexed)

#sort 매개변수 
result_sorted = employee_data.groupby('department', sort=True)['salary'].mean()
print(result_sorted)

result_No_sorted = employee_data.groupby('department', sort=False)['salary'].mean()
print(result_No_sorted)




# describe() 매서드
result = employee_data.groupby('department')['salary'].describe()
print(result)


employee_detail = pd.DataFrame({
    'department': ['Dev', 'Dev', 'Dev', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid', 'Senior'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'salary': [4000, 4500, 5500, 3800, 4300, 5200, 4500, 5300]
})

multy_group = employee_detail.groupby(['department', 'position'])['salary'].mean()
print(multy_group)

# agg() 다양한 사용법
# 1. 함수 이름 리스트
result1 = employee_detail.groupby(['department'])['salary'].agg(['mean', 'sum', 'std'])
print(result1)

# 값은 나오는데 사용은 안하는게 나을듯??
# result2 = employee_detail.groupby(['department'])['salary'].agg([np.mean, np.sum, np.std])
# print(result2)

# 3. 딕셔너리로 컬럼별 다른 함수

result2 = employee_detail.groupby('department').agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean')
)
