def solution(a, b, n):
    answer = 0
    while n // a != 0:
        for i in range(n, 0, -1):
            if i % a == 0:
                answer += i // a * b
                n = n - i + ((i // a) * b)
                break
    return answer


a = 3
b = 1
n = 20
print(solution(a, b, n))
