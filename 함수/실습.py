import numpy as np

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

# 1. a + b
print(a + b)

# 2. a - b
print(a - b)

# 3. a * 3
print(a * 3)

# 4. a의 크기(노름)
r = np.linalg.norm(a)
print("4: ", r)

# 5. a의 단위 벡터
r = a / r
print("5: ", r)




import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

B = np.array([[1, 2, 3],
              [4, 5, 6]])


print()
print("실습2")

# 1. A의 shape 확인
print(A.shape)
print()

# 2. A의 전치 행렬
A_T = A.T
print(A_T)
print(
    3
)

# 3. A @ B (가능한지 확인)
# A: (3, 2), B: (2, 3) → 가능
AB = A @ B
print(AB)
print()

# 4. B @ A
# B: (2, 3), A: (3, 2) → 가능
BA = B @ A
print(BA)
print()

# 5. np.arange(12)를 3×4 행렬로 reshape
C = np.arange(12).reshape(3, 4)
print(C)
