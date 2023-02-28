def solution(n):
    answer = 0
    b = ''
    while n != 0:
        b += str(n % 3)
        n //= 3
    b = b[-1::-1] #계산의 편의성을 위해 뒤집기
    for i in range(len(b)):
        answer += 3 ** i * int(b[i])
    return answer