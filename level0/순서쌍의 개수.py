def solution(n):
    answer = 0
    hint = []
    for i in range(1,n+1):
        if n % i == 0:
            hint.append((i,n/i))
    answer = len(hint)
    return answer