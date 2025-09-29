import numpy as np  # Numpy 패키지를 np로 임포트

# numpy(numberiacl python)는 파이썬에서 과학계산을 위한 핵심 라이브러리
# 데이터 과학, 머신러닝, 과학 연구 분야에서 가장 중요한 도구 중 하나 입니다.

# numpy 사용 이유
''' 
1. 속도 문제 해결 
파이썬은 인터프리터 언어로 실행 속도가 느립니다. 
Numpy는 c언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리 


2. 메모리 효율성
파이썬 리스트 : 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
Numpy배열 : 연속된 메모리 공간에 같은 타입의 데이터를 저장

3. 벡터화 연산
반복문 없이 전체 배열에 대한 연산을 한번에 수행
'''

print('Numpy 버전 :', np.__version__)
print('Numpy 설치 경로 : ', np.__file__)

# ndarray(N-dimensional array) Numpy의 핵심 자료 구조
# 같은 타입의 요소들을 담는 다차원 컨테이너

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print('1, 객체 타입: ', type(arr))  # <class 'numpy.ndarray'>
print('2, 데이터 타입: ', arr.dtype)  # int64
print('3, 배열 타입: ', arr.shape)  # (5,)
print('4, 차원 타입: ', arr.ndim)  # 1
print('5, 전체 타입: ', arr.size)  # 5


python_list = [1, 2.5, '3.', True]
numpy_array = np.array([1, 2.5, '3.', True])  # 자동으로 하나의 type으로 변경

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('리스트 더하기 :', list1 + list2)

list1 = np.array([1, 2, 3])
list2 = np.array([4, 5, 6])
print('Numpy 배열 더하기 :', list1 + list2)

#
int_array = np.array([1, 2, 3, 4, 5])
print('정수 배열 :', int_array)
print('데이터 타입: ', int_array.dtype)


float_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print('실수 배열 :', float_array)
print('데이터 타입: ', float_array.dtype)

# 타입을 명시적으로 지정 배열
specified_float_array = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print('명시적 배열 :', specified_float_array)
print('데이터 타입: ', specified_float_array.dtype)

# 문자열 배열
string_array = np.array(['apple', 'banana', 'cherry'])
print('문자열 배열 :', string_array)
print('데이터 타입: ', string_array.dtype)

# 2차원 배열 (3x3 행렬)
matrix = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])

print('2차원 배열(행렬) :', matrix)
print('모양 :', matrix.shape)
print('차원:', matrix.ndim)
print('크기:', matrix.size)


# 기존방식
# for i in ramge(3):
#     for j in range(3):
#         print()


rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)]
    rows.append(row)

matrix2 = np.array(rows)
print('동적 생성 행렬', matrix2)

# 3차원 배열
# (2x3x4)
tensor = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                   [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
print('3차원 배열 모양 :', tensor.shape)
print('3차원 배열 차원 :', tensor.ndim)

# numpy 내장 함수로 배열 생성
# 0부터 9까지
# 연속된 숫자 배열 arange
arr1 = np.arange(10)
print('0부터 9까지', arr1)

arr2 = np.arange(1, 11)
print('1부터 10까지', arr2)

arr3 = np.arange(1, 21, 2)
print('1부터 20까지 홀수만', arr3)

# 균등 간격 배열 linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5)
print('0부터 10까지 균등하게 5개 요소', arr1)

arr2 = np.linspace(0, 10, 5, endpoint=False)
print('끝값 제외', arr2)  #

# 로그 간격 배열 logspace


# zeros : 0으로 채워진 배열
zeros_1d = np.zeros(5)
print('1차원 0배열 :', zeros_1d)

zeros_2d = np.zeros((3, 4))
print('2차원 0배열 :\n', zeros_2d)

zeros_2d_int = np.zeros((3, 4), dtype=int)
print('2차원 0배열 :\n', zeros_2d)

# 2차원 배열 (3x3 행렬)
matrix = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])

# 기존 배열과 같은 모양의 영(0) 배열 생성
zeros_like = np.zeros_like(matrix)
print('matrix와 같은 모양의 0배열 :\n', zeros_like)


# ones : 1로 채워진 배열
# 1차원 1배열
ones_1d = np.ones(5)
print('1차원 1배열 :', ones_1d)

# 2차원 1배열
ones_2d = np.ones((3, 4))
print('2차원 1배열 :\n', ones_2d)

# 2차원 일 배열(3,4) bool타입
ones_2d_bool = np.ones((3, 4), dtype=bool)
print('2차원 1배열 :\n', ones_2d_bool)

# full
full_array = np.full((3, 4), 7)
print('2차원 배열: ', full_array)

full_like = np.full_like(matrix, 999)
print('2차원 배열:', full_like)

# 메모리만 할당, 값은 쓰레기값
empty_array = np.empty((2, 3))
print('2차원 배열: 쓰레기값', empty_array)


# 3 x 3 항등 행렬
identity = np.eye(4)
print('3x3 항등 행렬 :\n', identity)

# 4 x 5 행렬에서 대각선이 1
matrix = np.eye(4, 5)
print('4 x 5 행렬에서 대각선이 1 :\n', matrix)

# 대각선 위치 조정 (k매개변수)
matrix_k1 = np.eye(4, k=1)
print('위쪽 대각선:  (k=1) :\n', matrix_k1)

matrix_k2 = np.eye(4, k=-1)
print('아래쪽 대각선:  (k=1) :\n', matrix_k2)

# 정방 항등 행력
identity = np.identity(4)
print('4 x 4 항등 행렬 :\n', identity)


# 0과 1 사이의 균일 분포
random_uniform = np.random.rand(3, 3)
print('0부터 1균일 분포 :\n', random_uniform)


# 특정 범위의 균일 분포 (예 : 10~20)
low, high = 10, 20
rnadom_range = low + (high - low) * np.random.rand(3, 3)
print('low부터 20 균일 분포 :\n', rnadom_range)


uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print('0부터 100 균일 분포 :\n', uniform)

# 정규 분포 난수
# 표준 정규 분포(평균 0 표준편차 1)
random_normal = np.random.randn(3, 3)
print('표준 정규 분포 :\n', random_normal)

# 평균 100, 표준편차 15인 정규 분포
mean, std = 100, 15
scores = mean + std*np.random.randn(1000)
print('표준 정규 분표\n', scores[:10])
print('평균 :', scores.mean())
print('표준편차 :', scores.std())

# 정수 난수
# 0이상 10미만의 정수 난수
random_int = np.random.randint(0, 10, size=(3, 4))
print('0이상 10미만의 정수 난수 :\n', random_int)

# 주사위 시뮬레이션(1~6)
dice = np.random.randint(1, 7, size=10)
print('주사위 시뮬레이션 :', dice)

# 시드 설정(재현 가능한 난수)
np.random.seed(42)
random1 = np.random.rand(5)
print('첫 번째 난수 1 :', random1)

np.random.seed(42)
random2 = np.random.rand(5)
print('두 번째 난수 2 :', random2)
print('난수 동일 :', np.array_equal(random1, random2))

rng = np.random.default_rng(seed=42)
random3 = rng.random((2, 3))
print('새로운 난수 생성기 :\n', random3)


