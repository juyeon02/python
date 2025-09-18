import time
import random

# ------------------------
# 1. 시간복잡도별 함수
# ------------------------

# O(1) : 리스트 첫 번째 값 꺼내기


def test_O1(arr):
    return arr[0]

# O(n) : 리스트에서 값 찾기


def test_On(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

# O(n^2) : 이중 반복문


def test_On2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


# ------------------------
# 2. 실행 시간 재기
# ------------------------
sizes = [300]  # 입력 크기 (n 값)

for n in sizes:
    arr = list(range(n))
    target = random.choice(arr)

    # O(1)
    start = time.time()    # 실행 전 시간 기록
    test_O1(arr)  # 0(1) 함수 실행
    end = time.time()  # 실행 후 시간 기록
    print(f"O(1), n={n} 실행 시간: {round((end-start)*1000, 4)} ms")
    # 실행에 걸린 시간 계산

    # O(n)
    start = time.time()
    test_On(arr, target)
    end = time.time()
    print(f"O(n), n={n} 실행 시간: {round((end-start)*1000, 4)} ms")

    # O(n^2)
    start = time.time()
    test_On2(300)  # n^2은 너무 오래 걸려서 n을 작게 줌
    end = time.time()
    print(f"O(n^2), n=300 실행 시간: {round((end-start)*1000, 4)} ms")
