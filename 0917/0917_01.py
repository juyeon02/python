# break
for i in range(3):
    if i == 2:
        # break를 만나면 for문을 종료 한다
        break
    print(i)

for i in range(10):
    print(i)
    break        # 0 만 출력

for i in range(10):
    if i % 2:
        continue  # 짝수만
    print(i)

for i in range(10):
    print(i)
    pass  # 아무 행동도 하지 않음


# for else 문

for i in range(10):
    print(i)
    if i == 4:
        break  # 4까지 출력

else:
    print('루프 정상 종료')


colors = ['rde', 'blue']
fruits = ['apple', 'banana']

for color in colors:
    for fruit in fruits:
        print(f'{color}, {fruit}')
