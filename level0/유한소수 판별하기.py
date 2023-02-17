def solution(a, b):
    yak = 0
    for i in range(a,0,-1):
        if a % i ==0 and b % i == 0:
            yak = i
            break
    b //= yak
    while b % 2 == 0:
        b /= 2
    while b % 5 == 0:
        b /= 5
    if b == 1:
        return 1
    else:
        return 2
