import numpy as np


# 1번
A = np.arange(1, 10).reshape(3, 3)
B = np.full((3, 2), 2)
result1 = A @ B
print(result1)
# [[12 12]
#  [30 30]
#  [48 48]]

# 2번
I = np.eye(4, dtype=int)
M = np.random.randint(0, 10, (4, 4))
result2 = I @ M
print("M:\n", M)
print("I @ M:\n", result2)
print("동일 여부:", np.array_equal(result2, M))   # True

# 3번
X = np.ones((2, 5), dtype=int)
Y = np.arange(5, 15).reshape(5, 2)
result3 = X @ Y
print(result3)
# [[35 40]
#  [35 40]]

# 4번
C = np.random.randint(0, 5, (3, 2))
D = np.random.randint(0, 5, (2, 3))
result4 = C @ D
print("C:\n", C)
print("D:\n", D)
print("곱 결과 Shape:", result4.shape)
print(result4)
# 예시:
# C:
# [[1 4]
#  [0 2]
#  [3 1]]
# D:
# [[2 0 4]
#  [3 1 1]]
# 결과 Shape: (3, 3)
# [[14  4  8]
#  [ 6  2  2]
#  [ 9  1 13]]







# =============================================================
# 1번
arr = np.array([[10, 20], [30, 40], [50, 60]])

# 1) ravel vs flatten
r1 = arr.ravel()
f1 = arr.flatten()
print("ravel 결과:", r1)     # [10 20 30 40 50 60]
print("flatten 결과:", f1)   # [10 20 30 40 50 60]

# 2) arr[0,0] 변경
arr[0,0] = 999
print("arr 변경 후 ravel:", r1)   # [999  20  30  40  50  60] ← ravel은 원본과 연결
print("arr 변경 후 flatten:", f1) # [10 20 30 40 50 60] ← flatten은 원본과 독립


# 2번 expand_dims
img = np.random.rand(32, 32)
expanded = np.expand_dims(img, axis=0)
print(expanded.shape)   # (1, 32, 32)


# 3번 squeeze
img = np.random.randint(0, 255, (1, 28, 28, 1))
squeezed = np.squeeze(img)
print(squeezed.shape)   # (28, 28)


# 4번 unique & reshape
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])
flattened = arr.ravel()
unique = np.unique(flattened)
reshaped = unique.reshape(1, -1)
print(reshaped.shape, reshaped)  
# (1, 4) [[1 2 3 4]]


# 5번
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]])  # (1, 10, 1)
arr1d = arr.reshape(-1)   # (10,)
unique_vals = np.unique(arr1d)
print(unique_vals)  # [1 2 3]


# 6번
arr = np.array([
    [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]],
    [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
])  # shape (2, 3, 4)

arr1d = arr.ravel()
unique_vals = np.unique(arr1d)
reshaped = unique_vals.reshape(-1, 1)
print(reshaped.shape, reshaped)  
# (9, 1) [[0]
#         [1]
#         [2]
#         [3]
#         [4]
#         [5]
#         [6]
#         [7]
#         [8]]









