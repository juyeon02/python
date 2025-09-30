import numpy as np

# 배열 모양 변경, 조작

arr_1d = np.array([1, 2, 3, 4, 5, 6])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print('shape', arr_1d.shape)  # 모양
print('ndim', arr_1d.ndim)  # 차원
print('size', arr_1d.size)  # 사이즈
print(arr_1d.reshape(3, -1))  # 4행, 열은 자동 계산

print('===2차원 배열===')
print('shape', arr_2d.shape)  # 모양
print('ndim', arr_2d.ndim)  # 차원
print('size', arr_2d.size)  # 사이즈


# 배열 인덱싱, 슬라이싱


arr = np.array([10, 20, 30, 40, 50, 60, 70])
print('원본 배열 arr:\n', arr)

# 팬시 인덱싱(Fancy indexing)
indices = [1, 4, 7]
print('인덱스 [1, 4, 7] 요소:', arr[indices])  # [20 50 70]

# 범위 초과시 인덱스 에러
# 양수 인덱스(0부터 시작 )
print('arr[0]:', arr[0])   # 10

arr[0] = 100
print('arr[0] 100으로 변경:', arr)  # [100  20  30  40  50  60  70]

# 음수 인덱스(뒤에서부터)
print('arr[-1]:', arr[-1])  # 70

# 배열 슬라이싱
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print('원본 배열 arr:\n', arr)

print('인덱스 2부터 5까지:', arr[2:5])  # [30 40 50]

# 슬라이싱으로 값 수정
arr[2:5] = 100
print('인덱스 2부터 5까지 100으로 변경:', arr)  # [10 20 100 100 100 60 70]
''' 리스트는 슬라이싱으로 수정 불가능 '''

# arr[2:5] = [10, 20,] '''에러! 값 개수 맞춰야 함'''

original = np.array([1, 2, 3, 4, 5,])
view = original[1:4]
print('original:', original)   # [1 2 3 4 5]
print('view:', view)           # [2 3 4]

view[0] = 10
view[1:] = 20
print('view 10, 20으로 변경:', original)   # [ 1 10 20 20  5]
''' 슬라이싱한 view를 수정하면 original도 같이 수정됨 '''

# 독립적인 복사본 필요한 경우
original = np.array([1, 2, 3, 4, 5,])
copy = original[1:4].copy()

copy[0] = 100
print('copy 100으로 변경:', original)   # [1 2 3 4 5]
print('copy:', copy)                 # [100   3   4]
''' copy() 메서드로 복사본 만들기 '''

# 2차원 배열 3 x 3
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('2차원 배열: \n', matrix)
print('0,0 요소 접근: \n', matrix[0, 0])  # 1
'''인덱스 범위 초과시 에러'''

print('-1,-2 요소 접근: \n', matrix[-1, -2])  # 8
print('0행 전체 접근: \n', matrix[0])        # [1 2 3]

print('여러 행 접근: \n', matrix[0:2])    # [[1 2 3] [4 5 6]]
print('여러 행 접근: \n', matrix[0:2][0:2])    # [[1 2 3] [4 5 6]]

print('여러 행, 여러 열 접근: \n', matrix[0:2, 1:3])  # [[2 3] [5 6]]

# 부분 행렬 추출
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print('matrix[:2, 1:]', matrix[:2, 1:])  # [[ 2  3  4  5] [ 7  8  9 10]]
print('matrix[::2, ::2]', matrix[::2, ::2])  # [[ 1  3  5] [11 13 15]]


# 2차원 배열에서 팬시 인덱싱
# 특정 행들 선택
row_indices = [0, 2, 3]
print('[0, 2, 3] 행 선택:\n', matrix[row_indices])  # [[ 1  2  3  4  5] [11 12 13 14 15] [16 17 18 19 20]]

# 특정 요소들 선택( 행, 열 인덱스)
row_indices = [0, 2, 2]
col_indices = [3, 2, 3]
print('특정 요소 선택:\n', matrix[row_indices, col_indices])  # [ 4 13 14]

arr = np.arra([1, 5, 4, 7, 2, 3])
print('4이상', arr[arr >= 4])  # [5 4 7]
print('2 미만 4이상', arr[arr >= 2 & arr < 4])  # [3]
print('2 미만 또는 4이상', arr[(arr < 2) | (arr >= 4)])  # [1 5 4 7 3]


matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print('원본 행렬\n', matrix)
print('9보다 큰 요소들 :\n', matrix[matrix > 9])  # [10 11 12 13 14 15 16 17 18 19 20]

print('첫번째 열이 4 이상인 행들   \n', matrix[matrix[:, 0] >= 4])  # [[ 6  7  8  9 10] [11 12 13 14 15] [16 17 18 19 20]]
print('  \n', matrix[matrix[0, :] >= 4])  # [[ 4  5] [ 9 10] [14 15] [19 20]]

matrix[matrix > 9] = 10
print('9보다 큰 요소들 10으로 변경:\n', matrix)  # [[ 1  2  3  4  5] [ 6  7  8  9 10] [10 10 10 10 10] [10 10 10 10 10]]


# 기본 산술 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print('덧셈 a + b:', a + b)  # [11 22 33 44 55]
print('뺄셈 a - b:', a - b)  # [-9 -18 -27 -36 -45]
print('곱셈 a * b:', a * b)  # [ 10  40  90 160 250]
print('나눗셈 a / b:', a / b)  # [0.1 0.1 0.1 0.1 0.1]
print('몫 a // b:', a // b)  # [0 0 0 0 0]
print('나머지 a % b:', a % b)  # [1 2 3 4 5]
print('거듭제곱 a ** b:', a ** b)  #

# 스칼라와의 연산
a = np.array([1, 2, 3, 4, 5])
scalar = 10

print('+ 스칼라', a + scalar)  # [11 12 13 14 15]
print('- 스칼라', a - scalar)  # [-9 -8 -7 -6 -5]
print('* 스칼라', a * scalar)  # [10 20 30 40 50]
print('/ 스칼라', a / scalar)  # [0.1 0.2 0.3 0.4 0.5]

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

print('행결 A \n', a)
print('행렬 B \n', b)
print('행렬 덧셈 A + B \n', a + b)  # [[ 8 10 12] [14 16 18]]
print('행렬 뺄셈 A - B \n', a - b)
print('행렬 곱셈 A * B \n', a * b)  # [[ 7 16 27] [40 55 72]]
print('행렬 나눗셈 A / B \n', a / b)

print('행렬 곱 A @ B \n', a @ b)

# 브로드 캐스팅 (Broadcasting)
''' 서로 다른 모양의 배열 간 연산을 가능하게 하는 기능'''
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 '브로드캐스트'됨

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]
                   [7, 8, 9]])

print('원본 행렬:\n', matrix)
print('행렬 + 스칼라:\n', matrix + scalar)  # 각 요소에 10이 더해짐


# 브로드 캐스팅 규칙
'''
1. 차원 수가 다르면 작은 쪽의 앞에 1을 추가
   (3,3) + (3, ) -> (1, 3)

2. 각 차원에서 크기가 1이거나 같아야 함 
호환 가능: (3, 1) & (1, 4) = (3, 4)
호환 불가: (3, 2) & (3, 4) -> 에러

'''

# 통계
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np.sum(arr)        # 합계
np.mean(arr)       # 평균
np.median(arr)     # 중앙값
np.std(arr)        # 표준편차
np.var(arr)        # 분산
np.min(arr)        # 최소값
np.max(arr)        # 최대값
np.argmin(arr)     # 최소값 인덱스
np.argmax(arr)     # 최대값 인덱스
np.ptp(arr)        # 최대값 - 최소값

print('누적 합', np.cumsum(arr))  # [ 1  3  6 10 15 21 28 36 45]
print('누적 곱', np.cumprod(arr))  # [        1         2         6        24       120      720     5040    40320   362880]


matrix = np.array([[1, 2, 3],
                   [4, 5, 6]
                   [7, 8, 9]])

print('행별 합(axis=1): \n', np.sum(matrix, axis=1))  # [ 6 15 24]
print('열별 합(axis=0): \n', np.sum(matrix, axis=0))  # [12 15 18]
print('행별 평균(axis=1): \n', np.mean(matrix, axis=1))  # [2. 5. 8.]
print('열별 평균(axis=0): \n', np.mean(matrix, axis=0))  # [4. 5. 6.]