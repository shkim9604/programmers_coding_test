def solution(n):
    answer = 1
    count = 1
    while 1:
        count *= answer
        if count > n:
            break
        answer += 1

    return answer - 1