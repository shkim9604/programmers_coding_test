def solution(a, b):
    answer = ''
    day = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}
    month = {0: 0, 1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213, 8: 244, 9: 274, 10: 305, 11: 335}
    num = month[a - 1] + b - 1
    answer = day[num % 7]
    return answer
