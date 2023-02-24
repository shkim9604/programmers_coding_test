def solution(s):
    answer = sorted(s,reverse=True)
    a = ''
    for i in answer:
        a += i
    return a