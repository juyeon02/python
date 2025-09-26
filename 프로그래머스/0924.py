'''def solution(array, n):
    # n과 각 원소의 차이를 튜플로 저장
    sub = [(abs(n - i), i) for i in array]
    sub.sort(key=lambda x: (x[0], x[1]))

    return sub[0][1]


solution([3, 10, 28], 20)'''

'''
def solution(s):
    count = {}
    s_list = []

    for i in s:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

    for i in s:
        if count[i] == 1:
            s_list.append(i)
            s_list.sort()

    return ''.join(s_list).sort()


print(solution("abcabcadc"))
'''


def solution(numbers):
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for key, value in num_dict.items():
        numbers = numbers.replace(key, value)

    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))  # 123456789
