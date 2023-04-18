def solution(n):
    answer = 0
    for i in range(1,n+1):
        hap = 0
        for j in range(i,n+1):
            hap += j
            if hap > n:
                break
            if hap == n:
                answer += 1
                break
    return answer