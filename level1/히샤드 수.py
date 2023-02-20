def solution(x):
    answer = True
    hap = 0
    for i in str(x):
        hap += int(i)
    if x % hap != 0:
        answer = False
    return answer