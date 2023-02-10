def solution(n):
    answer = []
    count = 2
    while n >= count:
        if n % count == 0:
            n = n // count
            answer.append(count)
        else:
            count += 1
    answer = list(set(answer))
    answer.sort()
    return answer