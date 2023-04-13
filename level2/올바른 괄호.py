def solution(s):
    answer = True
    stack = []
    if s[0] == ")":
        answer = False
    if s[-1] == "(":
        answer = False
    for i in s:
        stack.append(i)
        if stack[0] == "(" and stack[-1] == ")":
            stack.pop()
            stack.pop()
    if len(stack) != 0:
        answer = False
    return answer