def solution(n):
    answer = 0
    pizza = 6
    while 1:
        if pizza % n == 0:
            answer = pizza // 6
            break
        else:
            pizza += 6
    return answer