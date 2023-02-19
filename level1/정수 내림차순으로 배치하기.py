def solution(n):
    answer = ''
    n = str(n)
    num = []
    for i in n:
        num.append(int(i))
    for i in range(len(num)):
        answer += str(max(num))
        num.remove(max(num))

    return int(answer)