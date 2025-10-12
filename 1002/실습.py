import pandas as pd

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
print(series + 10)
