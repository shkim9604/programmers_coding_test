def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        if str(k) in str(a):
            answer += str(a).count(str(k))
    return answer