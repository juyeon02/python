import numpy as np

# 실습2. 인덱싱과 슬라이싱

# 1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택하세요.
arr = np.arange(10, 30, 2)
print('1번: ', arr[[1, 3, 5]])  # [12 16 20]
print()

# 2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
arr = np.arange(1, 10).reshape(3, 3)
print('2번: ', arr[[0, 1, 2], [0, 1, 2]])  # [1 5 9]
print()

# 3. 3x4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
arr = np.arange(1, 13).reshape(3, 4)
arr[:, -1] = -1
print('3번 : \n', arr)
print()

# 4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('4번: 행 역순 : \n ', arr[::-1])
print()
print('4번: 열 역순 : \n ', arr[:, ::-1])
print()

# 5. 4x5 배열에서 가운데 2x3 부분을 슬라이싱한 뒤 copy()를 이용해 독립 배열을 만드세요.
arr = np.arange(1, 21).reshape(4, 5)
mid_arr = arr[1:3, 1:4].copy()
print('5번: \n', mid_arr)
print()

# 6. 3x4 배열에서 짝수이면서 10 이상인 값만 선택하세요.(&을 활용)
arr = np.array([[4, 9, 12, 7], [10, 15, 18, 3], [2, 14, 6, 20]])
print('6번 : \n', arr[(arr % 2 == 0) & (arr >= 10)])
print()

# 7. 5x5 배열에서 2, 4번째 행을 선택하고, 선택된 행에서 열 순서를 [4, 0, 2]로 재배치하세요.
arr = np.arange(1, 26).reshape(5, 5)
print('7번:\n', arr[[1, 3]][:, [4, 0, 2]])
# 열 순서 재배치 : [:, [4, 0, 2]]
print()

# 8. 5x3 배열에서 각 행의 첫 번째 값이 50 이상인 행만 Boolean Indexing으로 선택하세요.
arr = np.array([[10, 20, 30], [55, 65, 75], [40, 45, 50], [70, 80, 90], [15, 25, 35]])
print('8번:\n', arr[arr[:, 0] >= 50])
print()

# 9. 4x4 배열에서 (0,1), (1,3), (2,0), (3,2) 위치의 요소를 한 번에 선택하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('9번:\n', arr[[0, 1, 2, 3], [1, 3, 0, 2]])
print()


# 10. 3차원 배열 (2, 3, 4)에서 모든 블록에서 두 번째 열만 추출해 새로운 2차원 배열 (2, 3)을
arr3d = np.arange(24).reshape(2, 3, 4)
arr2d = arr3d[:, :, 1]
print('10번:\n', arr2d.reshape(2, 3))
print()

# ===================================================
print('실습3. NumPy 종합 연습')
# 1. 0부터 24까지 정수를 가진 배열을 만들고, (5, 5) 배열로 변환한 뒤 가운데 행(3번째 행)과 가운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
arr = np.arange(0, 25).reshape(5, 5)
print('1번 행: \n', arr[2:3, :])
print('1번 열: \n', arr[:, 2])
print()

# 2. 0~99 난수로 이루어진 (10, 10) 배열을 생성하고, 짝수 인덱스의 행만 선택하여 출력하세요.
arr = np.random.randint(0, 99, (10, 10))
print('2번: \n', arr[::2])
print()

# 3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후, 2행 3열부터 4행 7열까지의 부분 배열을 추출하세요
arr = np.arange(50).reshape(5, 10)
print('3번: \n', arr[1:4, 2:7])
print()

# 4. 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
arr = np.random.randint(0, 9, (4, 4))
# • 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
arr1 = [arr[i, i] for i in range(4)]
# • 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
arr2 = [arr[i, 3-i] for i in range(4)]
print('4번 주대각선: \n ', arr1)
print('4번 부대각선: \n', arr2)
print()

# 5. 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고, 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요
arr = np.random.randint(0, 10, (3, 4, 5))
print('5번 첫번째 행 마지막 열: \n', arr[1, 0, -1])

print()

# 6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10x4 행렬로 변환 후 출력해 주세요.
arr6 = np.arange(35, 75).reshape(10, 4)
print('6번: \n', arr6)
print()

# 7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
print('7번: \n', arr6[::-1, :])
print()

# 8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지, 세번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.
print('8번: \n', arr6[1:-1, 2:])
print()

# 9. 1부터 50까지의 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성하세요.
arr = np.random.randint(1, 51, (5, 6))
print('9번: \n', arr[arr % 2 == 0])
print()

# 10. 0부터 99까지의 정수로 이루어진 (10, 10) 배열을 생성한 후, [1, 3, 5]번째 행과 [2, 4, 6]번째 열의 교차하는 원소들만 선택하여 출력하세요.
arr = np.arange(0, 100).reshape(10, 10)
rows = [1, 3, 5]  # 행
cols = [2, 4, 6]  # 열

arr1 = []
for r in rows:           # 행 순회
    row_data = []        # 한 행씩 담을 리스트
    for c in cols:       # 열 순회
        row_data.append(arr[r, c])
    arr1.append(row_data)

arr1 = np.array(arr1)

print('10번: \n', arr1)
print()


# 11. 0~9 난수로 이루어진 1차원 배열(길이 15)을 생성하고, 짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
arr = np.random.randint(0, 10, 15)
arr1 = arr[::2]
print('11번 짝수 인덱스 값: \n', arr1)
print('11번 짝수 인덱스 중 5 이상인 값: \n', arr1[arr1 >= 5])
print()


# 실습1. 배열 연산
# 1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
print('1번: ', arr + 3)  # [4 5 6 7]
print()

# 2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10], [15, 20]])
print('2번: \n', arr * -1)
print()

# 3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
print('3번 곱셈: ', arr1 * arr2)
print('3번 나눗셈: ', arr1 / arr2)


# 4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해 필요한 값을 더한 결과 배열을 브로드 캐스팅으로 만드세요.
arr = np.array([[95, 97], [80, 85]])
arr2 = np.array([(100-arr)])
print('4번: \n', arr + arr2)


print()
# 5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
arr = np.array([[1, 2, 3], [4, 5, 6]])
# 첫 번째 행은 10을 곱하고
# 두 번째 행은 100을 곱해야 합니다.
arr2 = np.array([[10,], [100,]])
print('5번: \n ', arr * arr2)


print()
# 6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# • 1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
# • 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.

arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])
arr2 = np.array([[100], [200], [300]])

print('6번:  \n', arr + arr2)
print()
print()
print()

print('실습2. 통계 함수 및 집계 연산')
# 1. 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print('1. 합계 : \n ', np.sum(arr))
print('1. 평균 : \n ', np.mean(arr))


print()
# 2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1], [9, 2, 8]])
print('2. 최소값 : \n ', np.min(arr))
print('2. 최대값 : \n ', np.max(arr))


print()
# 3. 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('3. 행별 평균 : \n ', np.sum(arr, axis=1))
print('3. 열별 평균 : \n ', np.sum(arr, axis=0))


print()
# 4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20], [30, 40], [50, 60]])
print('4. 행별 평균 : \n ', np.mean(arr, axis=1))
print('4. 열별 평균 : \n ', np.mean(arr, axis=0))


print()
# 5. 1차원 배열에서 전체 표준편차를 구하고, 각 요소가 평균으로부터 얼마나 떨어져 있는지
# 편차 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print('5. 표준편차 : \n ', np.std(arr))
print('5. 편차 배열 : \n ', arr - np.mean(arr))


print()
# 6. 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('6. 누적 합 : \n', np.cumsum(arr, axis=1))
print('6. 누적 곱 : \n', np.cumprod(arr, axis=0))
