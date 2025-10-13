import pandas as pd

# DataFrame vs Series

# Series
# 1차원

# DataFrame
# 2차원(Series들의 묶음)
# 데이터(values) - 2차원 배열
# 행 인덱스(index) - 각 행의 레이블
# 열 이름(columns) - 각 열의 레이블

df_default = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 26, 27]
})

print(f'인덱스: {df_default}')
print(f'인덱스: {df_default.index}')
print(f'인덱스: {df_default.columns.tolist}')

# =======================================================

# CSV
# CSV(comma-Separated Values) 가장 널리 사용되는 데이터 파일 형식

# 특징
'''
쉼표(,) 로 값을 구분 
텍스트 파일이라 어디서나 열람 가능 
가볍고 빠름 
Excel, Google Sheets 등과 호환 
'''
'''
df = pd.read_csv('sample_data.csv')
print(df)'''

sample_data = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 26, 27],
    'city': ['Seoul', 'Busan', 'Daegu'],
    'salary': [50000, 60000, 55000]
})

sample_data.to_csv('sample_data.csv', index=False , encoding='utf-8')

# utf-8-sig : UTF8 + BOM(Excel 호환)
'''
df = pd.read_csv('sample_data.csv' , encoding='utf-8')
print(df)
'''
# sep - 구분자 설정
sample_data.to_csv('tab_separated.txt', sep='\t', index=False)

df_tab = pd.read_csv('tab_separated.txt', sep='\t')
print(df_tab)

# print(df_tab.head()) # 처음 5개 행

# Excel 은 마이크로소프트의 스프레드시트 프로그램
'''
여러 시트 지원
서식, 수식 포함 가능
비즈니스에서 가장 많이 사용
확장자(.xlsx)(.xls)
'''


sample_data = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 26, 27],
    'city': ['Seoul', 'Busan', 'Daegu'],
    'salary': [50000, 60000, 55000]
})

sample_data.to_excel('sample_data.xlsx', index=False, sheet_name='Default')
print('샘플 엑셀 파일 생성 완료')

df_excel = pd.read_excel('sample_data.xlsx')
print(df_excel)

with pd.ExcelWriter('muti_sheet.xlsx') as writer:

    sample_data.to_excel(writer, sheet_name='Default1')
    sample_data['name'].to_excel(writer, sheet_name='name', index=False)


# JSON
# 웹에서 많이 사용되는 데이터 형식

sample_data = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 26, 27],
    'city': ['Seoul', 'Busan', 'Daegu'],
    'salary': [50000, 60000, 55000]
})

sample_data.to_json('sample_data.json', orient='records', indent=2)
print('JSON 파일 저장')

df_json = pd.read_json('sample_data.json')
print(df_json)
