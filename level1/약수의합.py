def solution(n):
    answer = 0
    count = 1
    for i in range(n):
        if n % count == 0:
            answer +=count
            count +=1
        else:
            count +=1
            continue
    return answer