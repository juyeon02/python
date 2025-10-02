# stack
'''
스택(stack) 후입선출(LIFO LAST IN FIRST OUT) 원칙을 따르는 선형 자료구조
가장 나중에 들어간 데이터가 가장 먼저 나오는 구조 -> 책을 쌓아놓는 것과 같은 형태 

스택은 한쪽 끝(top) 에서만 데이터의 삽입과 삭제가 일어난다
'''

# 핵심특징
'''
1. LIFO : 가장 최근에 추가된 요소가 가장 먼저 제거
2. 제한된 접근
스택의 요소들은 오직 TOP을 통해서만 접근 가능합니다. 
중간 요소에 직접 접근할 수 없습니다. 
3. 주요 연산의0(1) 시간 복잡도
push와 pop연산 모두 0(1)의 시간 복잡도를 가진다
4. 메모리 효율성
동적 배열이나 연결 리스트로 구현 가능, 필요에 따라 크기를 조절 할 수 있다
'''

# push(data) 스택의 맨 위에 요소 초가
# pop() 스택의 맨 위 요소 제거 및 반환
# peek() / top() 맨 위 요소 확인( 제거 x )
# is_empty() 스택이 비어있는지 확인
# sizw() 스택의 요소 개수 반환

'''
class Stack:
    def __init__(self):
        # 스택 초기화
        self.items = []

    def push(self, item):
        # 요소 추가
        self.items.append(item)

    def pop(self):
        # 요소 제거 및 반환
        if not self.is_empty():
            return self.irems.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        # 맨 위 요소 확인
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items) == 0

    def __str__(self):
        # 스택출력
        return str(self.items) == 0


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f'스택: {stack}')
print(f'스택: {stack.pop()}')
print(f'스택: {stack}')
print(f'스택: {stack.peek()}')
print(f'스택: {stack}')
print(f'스택: {stack}')

'''
'''class Stack:
    def __init__(self):
        # 스택 초기화
        self.items = deque()

    def push(self, item):
        # 요소 추가
        self.items.append(item)

    def pop(self):
        # 요소 제거 및 반환
        if not self.is_empty():
            return self.irems.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        # 맨 위 요소 확인
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items) == 0

    def __str__(self):
        # 스택출력
        return str(self.items) == 0'''


# 큐(queue)
'''
큐는 선입선출 원칙을 따르는 선형 자료 구조
가장 먼저 들어간 데이터가 가장 먼저 나오는 구조 -> 줄서기 형태 
큐는 한쪽 끝(Rear)에서 삽입이 일어나고 다른 쪽 끝(Front)에서 삭제가 일어납니다. 
'''

# 핵심 특징
'''
1. FIFO : 가장 먼저 추가된 요소가 가장 먼저 제거 됩니다. 큐의 근본적인 특징
2. 양 끝 접근  : 큐는 rear(뒤)에서 삽입(enqueue)이, front(앞)에서 삭제(dequeue)가 일어납니다. 
3. 순차적 처리 : 작업들을 순서대로 처리해야 할 때 유용합니다.
4. 공평한 자원 분배 : 먼저 요청한 작업이 먼저 처리되는 공정성을 보장


'''

# enqueue(item) : 큐의 뒤쪽에 요소 추가
# dequeue() : 큐의 앞쪾 요소 제거 및 반환
# front() / peek() : 맨 앞 요소 확인
# is_empty() : 큐가 비어있는지 확인
# sizw() : 큐의 요소 개수 반환


# 비효율적_ 리스트로 구현
from collections import deque
class ListQeueu:
    def __init__(self):
        self.items = []
        # 리스트 기반 큐(비효율적)

    def enqueue(self, item):
        # 요소 추가
        self.items.append(item)

    def dequeue(self):
        # 요소 제거
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError('Queue is empty')

    def is_empty(self):
        # 비어있는지 확인
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


queue = ListQeueu()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'Queue: {queue}')


# 덱(Deque)
'''
덱(Deque, Double_Ended Queue)
양쪽 끝에서 삽인봐 삭제가 모두 가능한 자료조
스택과 큐의 특성을 모두 가지고 있어, 매우 유연한 자료구조
'deck'으로 발음
'''

# 특징
'''
1. 양방향 연산(Double_ended)
앞쪽(front) 뒤쪽(rear) 모두에서 요소의 추가, 제거가 가능하다.

2. 0(1) 시간 복잡도
양쪽 끝에서의 모든 연산이 상수 시간에 수행된다. 

3. 동적 크기
필요에 따라 크기가 자동으로 조절

4. 스택과 큐 동시 구현 
하나의 자료구조로 스택과 큐를 모두 구현할 수 있다.

5. 회전 연산 지원
요소들을 좌우로 회전시킬 수 있습니다. 

'''

# 주요 연산
'''
append(x) 오른쪽 끝에 요소 추가
appendleft() 왼쪽 끝에 요소 추가

pop() 오른쪽 끝 요소 제거 및 반환
popleft() 왼쪽 끝 요소 제거 및 반환

extend(iterable) 오른쪽에 여러 요소 추가
extendleft(iterable) 왼쪽에 여러 요소 추가


rotate(n) n 만큼 회전
clear() 모든 요소 제거
'''

# 회문(pallindrome) 검사
''' 앞 뒤가 똑 같은 '''


# from collections import deque

def is_palindrome(s):
    # 덱을 이용한 회문 검사
    
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

is_palindrome('level') # True
is_palindrome('tomato') # False



