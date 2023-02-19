def solution(n):
    answer = n ** 0.5
    if answer - int(answer) == 0:
        answer = pow(answer+1,2)
    else:
        answer = -1
    return answer