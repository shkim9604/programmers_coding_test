def solution(sides):
    answer = 0
    result = []
    for i in range(1, max(sides) + 1):
        if i + min(sides) > max(sides):
            result.append(i)
    for i in range(sum(sides), max(sides)-1, -1):
        if i < sum(sides):
            result.append(i)
    result = set(result)
    answer = len(result)
    return answer