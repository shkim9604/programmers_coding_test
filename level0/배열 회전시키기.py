def solution(numbers, direction):
    answer = []
    if direction == "right":
        a = numbers[-1]
        numbers.pop()
        numbers.insert(0,a)
    else:
        a = numbers[0]
        numbers.remove(numbers[0])
        numbers.append(a)
    answer = numbers
    return answer