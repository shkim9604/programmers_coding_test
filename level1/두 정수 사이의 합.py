def solution(a, b):
    big = 0
    small = 0
    sum = 0
    if a > b:
        big = a
        small = b
    else:
        small = a
        big = b
    sum = sum + small
    for i in range(big-small):
        sum += small+1
        small += 1
    answer = sum
    return answer