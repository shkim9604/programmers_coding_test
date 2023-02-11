def solution(balls, share):
    answer = 0
    a = 1
    for i in range(balls,0,-1):
        a *= i
    b = 1
    c = 1
    for i in range(balls-share,0,-1):
        b *= i
    for i in range(share,0,-1):
        c *= i
    answer = a // (b * c)
    return answer