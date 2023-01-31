def solution(numbers):
    answer = 0
    numbers.sort()
    a = max(numbers)
    numbers.pop()
    b = max(numbers)
    answer = a * b
    return answer