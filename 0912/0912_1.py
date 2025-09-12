# 인덱싱 - 문자열

'''list1 = list()
list2 = list("Hello")

# H  e  l  l  o
# 0  1  2  3  4
# 0 -4 -3 -2 -1

print(list1)
print(list2)

print('인덱스0: ', list2[0])
print('인덱스0: ', list2[-1])

list[4] = 'a'
print(list)'''


'''list3 = list("python")

print(list3[:])

numbers = [10, 20, 30, 40]
print('numbers[:3:2]', numbers[:3:2])
print('numbers 뒤집기', numbers[::-1])'''


letters = ["A", "B"]
letters3 = letters * 3
del letters3[2]
print(letters3)


# 인덱스 요소를 삭제
'''del list1[3]'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

result = list1 * 3
print(result)


print(1 in list1)


# 요소 추가 메서드
numbers = [10, 21, 15, 22, 54]

numbers.append(20)
print(numbers)

# 여러 요소를 추가할 때
numbers.extend([19, 5])
print(numbers)

numbers.extend([5.29])
print(numbers)

# append - extend 차이점
# append - 리스트 자체가 추가됨
# extend - 요소들이 추가됨


# 삭제 메서드

fruits = ['사과', '바나나']

fruits.clear()  # 모든 요소 제거
print(numbers)


# 요소 검색, 정렬 메서드
numbers = [1, 2, 4, 6, 8, 2, 1, 7]

idx = numbers.index(6)  # 자리 찾기
print("idx: ", idx)

count = numbers.count(2)
print('count: ', count)

numbers.sort()  # 오름차순
print('numbers: ', numbers)

numbers.sort(reverse=True)  # 내림차순
print('numbers: ', numbers)

# sorted
original = [3, 2, 5, 7, 1]
sorted_list = sorted(original)

print(original)
print(sorted_list)


# 연산 메서드
numbers = [5, 2, 7, 3, 11, 45]
max_num = max(numbers)  # 최대
min_num = min(numbers)  # 최소
sum_num = sum(numbers)  # 총합
