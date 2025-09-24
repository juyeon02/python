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
