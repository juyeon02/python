import numpy as np
# 실습1. 배열 초기화 및 생성(1)
# 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요.
zero = np.zeros((3, 4))
print('0으로 채워진 크기 (3,4) 배열 :\n', zero)

five = np.full((3, 4), 5)
print('1번 : 모든 값을 5로 채운 배열 :\n', five)

# 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
arr = np.arange(0, 21, 2)
print('2번: 0부터 20까지 2씩 증가하는 1차원 배열 :', arr)

# 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
random_array = np.random.rand(2, 3)
print('3번 : 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열 :\n', random_array)


# 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하세요
# nomal(평균, 표준편차, 사이즈)
normal_array = np.random.normal(100, 20, 6)
print('4번: 평균이 100, 표준편차가 20인 정규분포 난수 6개 :', normal_array)

# 1부터 20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4, 5) 크기의 2차원 배열로
array_1d = np.arange(1, 21)
array_2d = np.eye(4, 5) * array_1d.reshape(4, 5)
print('5번: 1부터 20까지의 정수를 포함하는 (4, 5) 크기의 2차원 배열 :\n', array_2d)


# 0부터 1까지 균등 간격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3, 4) 크기로 변환
# reshape() _ 재배치 : 요소의 모양을 다시 잡아준다. 대신 요소의 개수가 맞게 들어있어야 함
linspace_array = np.linspace(0, 1, 12)
linspace_array = linspace_array.reshape(3, 4)
print('6번: 0부터 1까지 균등 간격으로 나눈 12개의 값을 가지는 (3, 4) 크기의 배열 :\n', linspace_array)

# 0~99 사이의 난수로 이루어진 (10, 10) 배열을 생성한 뒤, np.eye()로 만든 단위 행렬을 더하여 대각선 요소가 1씩 증가된 배열을 만드세요.
random_10x10 = np.random.randint(0, 100, (10, 10))
identity_matrix = np.eye(10)
result_array = random_10x10 + identity_matrix
print('7번 ㅣ 대각선 요소가 1씩 증가된 배열 :\n', result_array)


# 0~9 사이의 난수로 이루어진 (2, 3, 4) 3차원 배열을 생성하세요.
array_3d = np.random.randint(0, 10, (2, 3, 4))
print('0~9 사이의 난수로 이루어진 (2, 3, 4) 3차원 배열 :\n', array_3d)
