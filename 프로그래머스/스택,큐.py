# 스택 _ 올바른 괄호
def solution(s):
    stack = 0
    for ch in s:
        if ch == '(':
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1

    return stack == 0


print(solution('(())(())'))
