'''
a = 10
a += 5
print(a)


text = "hi!"
print(text * 3)
'''
"""
name = input("이름을 입력하세요: ")
print(name)

score = int(input("점수를 입력하세요: "))
print(f'점수는 : {score + 10}')

# 연산을 할 때 문자 + 숫자는 계산이 안되기 때문에 int() 사용
"""

# split() : 공백을 구분자로 나누겠다

fruit = "사과 참외 수박 ".split()
print(fruit)


fruit1, fruit2, fruit3 = input() .split()
print(fruit1, fruit2, fruit3, sep=",")
