def solution(numbers, k):
    answer = 0
    loc = k * 2 -1
    answer = numbers[loc % len(numbers) - 1]
    return answer