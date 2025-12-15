import pandas as pd
'''
# 실습1. Series 연습
# 1. 파이썬 리스트 [5, 10, 15, 20]을 이용해 Series를 생성하세요.
data = [5, 10, 15, 20]
series = pd.Series(data)
print(series)

# 2. 값 [90, 80, 85, 70]에 대해 인덱스를 각각 '국어', '영어', '수학', '과학'으로 지정한 Series를 만드세요.
data2 = pd.Series([90, 80, 85, 70], index=['국어', '영어', '수학', '과학'])
print(data2)

# 3. {'서울': 950, '부산': 340, '인천': 520} 딕셔너리를 이용해 Series를 만들고, 인천의 값을 출력하세요
data3 = {'서울': 950, '부산': 340, '인천': 520}
print(data3['인천'])

# 4. Series [1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
series = pd.Series([1, 2, 3, 4])
print(series.dtype)


# 5. 아래 두 Series의 합을 구하세요.
s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])

result = s1 + s2
print(result)

# 6. Series [1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
series = pd.Series([1, 2, 3, 4, 5])
print(series + 10)'''


# 실습2. DataFrame 연습(1)
# 1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
df1 = pd.DataFrame(
    [['홍길동', 28, '서울'],
     ['김철수', 33, '부산'], ['이영희', 25, '대구']],
    columns=['이름', '나이', '도시']
)
print(df1)
print()

# 2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df2 = pd.DataFrame(data)
print(df2)
print()

# 3. 아래 데이터를 사용해 DataFrame을 만드세요.
data = [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
df3 = pd.DataFrame(data)
print(df3)
print()

# 4. 아래 데이터를 사용해 DataFrame을 생성하되, 인덱스를 ['학생1', '학생2', '학생3']으로 지정하세요.
df4 = pd.DataFrame({'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]}, index=['학생1', '학생2', '학생3']
)
print(df4)
print()

# 5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])
df5 = pd.DataFrame({'kor': kor, 'eng': eng})
print(df5)
print()

# 6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
df6 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}
)
print(df6[['B', 'A']])
print()

# 7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
df7 = pd. DataFrame([['펜', 1000, 50], ['노트', 2000, 30]], columns=['product', 'price', 'stock']
)
print(df7)
print()

# 8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
df8 = pd.DataFrame({'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
)
print(df8['국가'])