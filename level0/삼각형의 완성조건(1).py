def solution(sides):
    a = max(sides)
    sides.remove(a)
    answer = a - sum(sides)
    if answer < 0:
        answer = 1
    else:
        answer = 2
    return answer