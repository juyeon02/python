'''# 합성수 찾기
n = 15
num = []

for i in range(n+1):
    if i % 2 == 0 :
        num.append(i)
    elif i % 3 == 0:
        num.append(i)
    elif i % 5 == 0:
        num.append(i)
    elif i % 7 == 0:
        num.append(i)
    else:
        pass

print(len(num))'''

'''n = 12
answer = []

while True:

    if n % 2 == 0:
        answer.append(2)
    elif n % 3 == 0:
        answer.append(3)
    elif n % 5 == 0:
        answer.append(5)
    elif n % 7 == 0:
        answer.append(7)
        break
    else:
        print([n])

    print(answer.sort(reverse=True))'''


'''n = 121
answer = []

# 2, 3, 5, 7로 나눌 수 있는 소인수만 추가
for i in range(2, n+1):
    if n % i == 0:
        if i not in answer:
            answer.append(i)
            n = n % i

    # 소인수가 없으면 n 자체를 추가
if not answer:
    answer.append(n)

answer.sort()
print(answer)
'''

s = '10 Z 20 Z 1'
answer = 0


for x in s.split():
    if x == "Z":
        if answer:        # 스택이 비어있지 않으면
            answer.pop()  # 마지막 숫자 제거
        else:
            answer += int(x)  # 숫자는 스택에 추가


print(sum(answer))
