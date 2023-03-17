def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        yak = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                if j == i // j:
                    yak += 1
                else:
                    yak += 2
        if yak > limit:
            answer += power
        else:
            answer += yak

    return answer
