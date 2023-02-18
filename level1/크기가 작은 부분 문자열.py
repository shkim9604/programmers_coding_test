def solution(t, p):
    answer = 0
    numbers = []
    index = 0
    while index != (len(t) - len(p) + 1):
        a = t[index:index + len(p)]
        index += 1
        numbers.append(a)
    print(numbers)
    for i in numbers:
        if int(i) <= int(p):
            answer += 1
    return answer

t = "500220839878"
p = "7"
print(solution(t,p))