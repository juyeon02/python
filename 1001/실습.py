import numpy as np
'''# 실습3. 논리 연산과 조건 연산
# 1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
arr = np.array([5, 12, 18, 7, 30, 25])
result = arr[(arr > 10) & (arr < 20)]
print('1번: ', result)


# 2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
arr = np.array([10, 15, 20, 25, 30, 35])
result = arr[(arr <= 15) | (arr >= 30)]

print('2번: ', result)


# 3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
arr = np.array([3, 8, 15, 6, 2, 20])
arr[arr >= 10] = 0
print('3번: ',  arr)

# 4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운 배열을 생성하세요
arr = np.array([7, 14, 21, 28, 35])
result = np.where(arr > 20, "High", "Low")
print('4번: ', result)



print()
print()
print()
print()
print()


# 5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr = np.arange(0, 10)
result = np.where(arr % 2 == 0, arr, arr*10)

print('5번: ', result)


# 6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
arr = np.array([[10, 25, 30], [40, 5, 15], [20, 35, 50]])
result = arr[(arr <= 40) & (arr >= 20)]

print('6번: ', result)


# 7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr = np.array([1, 2, 3, 4, 5, 6])
resuslt = arr[~(arr % 3 == 0)]

print('7번: ', resuslt)

# 8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# 50 이상인 값은 그대로
# 50 미만인 값은 50으로 변경
arr = np.random.randint(0, 101, 10)
result = np.where(arr >= 50, arr, 50)

print('8번: ', result)

# 9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# 70 이상 → "A"
# 30 이상 70 미만 → "B"
# 30 미만 → "C“
arr = np.array([[5, 50, 95], [20, 75, 10], [60, 30, 85]])
result = np.where(arr >= 70, 'A', np.where(arr >= 30, 'B', 'C'))
print('9번: ', result)


# =================과제 =============
print('실습1. 배열 형태 변형, 차원 확장·축소(1)')
# 1. ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
# arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
arr = np.array([[10, 20], [30, 40], [50, 60]])
print('1번')
rav = arr.ravel()
fla = arr.flatten()

print('ravel', rav)
print('flatten', fla)

arr[0, 0] = 999
print('ravel', rav)
print('flatten', fla)

print()

# 2. 크기가 32x32인 이미지 데이터를 가정하고,
# 이 배열에 대해 expand_dims를 사용하여 shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img = np.random.rand(32, 32)
arr = np.expand_dims(img, axis=0)
print('2번: \n ', arr.shape)
print()

# 3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img = np.random.randint(0, 255, (1, 28, 28, 1))
arr = np.squeeze(img)
print('3번: \n ', arr.shape)
print()

# 4. 아래 2차원 배열을
# shape (1, n)으로 재구성하세요.
arr = np.array([[3, 1, 2, 2], [1, 2, 3, 1], [2, 2, 1, 4]])
flat = arr.flatten()  # 1) 1차원 배열로 만든 후
uniq = np.unique(flat)  # 2) 중복값을 제거한 뒤
arr4 = np.expand_dims(uniq, axis=0)
print('4번: \n ', arr4.shape)
print()

# 5. 다음 배열을 shape (10,)로 만든 뒤 고유값 배열을 구하세요.
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]])  # shape (1, 10, 1)
squeezed = np.squeeze(arr)
uniq = np.unique(squeezed)
print('5번: \n ', uniq)
print()


# 6. 다음 배열을 1차원 배열로 만든 후 고유값만 추출해서 shape (고유값 개수, 1)인 2차원 배열로 변환하세요.
arr = np.array([[[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]], [
               [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]])  # shape (2, 3, 4)
print('6번: \n ',)
print()

'''
# =======================================================================================
print()
print('실습2. 배열의 결합과 분리(1)')
# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.concatenate((a, b), axis=0)
print('1번: \n ', result)
print()

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
arr = np.split(a, 3)
print('2번')
for i, sub in enumerate(arr):
    print(i+1, sub)

print()

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
result = np.stack((a, b, c), axis=0)
print('3번: \n ', result)
print()

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
arr = np.stack((a, b), axis=0)
print('4번: \n ', arr)
print()


# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
arr = np.arange(8)
arr5 = np.split(arr, [2, 5], axis=0)
print('5번')
for i, a in enumerate(arr5):
    print(i+1, a)
print()


# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요
a = np.ones((2, 3))
b = np.zeros((2, 3))
print('6번 axis = 0: \n ', np.stack((a, b), axis=0).shape)
print('6번 axis = 1: \n ', np.stack((a, b), axis=1).shape)
print()


# =======================================================================================
print()
print('실습3. 배열의 정렬(1)')
# 1. 아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
arr = np.array([7, 2, 9, 4, 5])
print('1번 오름차순: \n ', np.sort(arr))
print('1번 내림차순: \n ', np.sort(arr)[::-1])
print()


# 2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[9, 2, 5], [3, 8, 1]])
print('2번: \n ', np.sort(arr))
print()


# 3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고, 그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
arr = np.array([10, 3, 7, 1, 9])
idx = np.argsort(arr)
print('3번 인덱스: \n ', idx)
print('3번: \n ', arr[idx])
print()

# 4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[4, 7, 2], [9, 1, 5], [6, 8, 3]])
print('4번: \n ', np.sort(arr, axis=0))
print()
