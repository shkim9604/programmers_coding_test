def solution(s):
    answer = -1
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer