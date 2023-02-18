numbers = [1, 2, 3, 4, 6, 7, 8, 0]
answer = 0
answer += (x for x in range(0, 10) if x not in numbers)
print(answer)
