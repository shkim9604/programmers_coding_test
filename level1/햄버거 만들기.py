def solution(ingredient):
    answer = 0
    buger = []
    for i in ingredient:
        buger.append(i)
        if buger[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                buger.pop()
    return answer