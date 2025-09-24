'''import time
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
'''


# deque_요세푸스 예제

'''
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

'''
# 리스트 사용시


from collections import deque
def josephus_list(N, K):
    people = list(range(1, N+1))
    result = []
    count = 0   # K번째를 세기 위한 카운트

    while people:
        for i in range(len(people)):
            count += 1
            if count == K:
                result.append(people.pop(0))  # 맨 앞 사람 제거
                count = 0
            else:
                # 맨 앞 사람을 뒤로 보내서 원형 유지
                people.append(people.pop(0))
    return result


# 데큐 사용시


def Josephus_dq(N, K):
    dq = deque(range(1, N+1))
    result = []

    while dq:
        # 제거해야 할 k번째 사람을 맨 앞으로 이동
        dq.rotate(-(K-1))
        result.append(dq.popleft())
    return result


# 데큐 실행 예시
N, K = 7, 3

print(josephus_list(7, 3))  # [3, 6, 2, 7, 5, 1, 4]

print(Josephus_dq(7, 3))  # [3, 6, 2, 7, 5, 1, 4]


weight[10, 1, 1]
