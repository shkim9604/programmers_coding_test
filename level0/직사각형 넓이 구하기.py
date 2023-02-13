def solution(dots):
    answer = 0
    point_w = dots[0][0]
    point_h = dots[0][1]
    for i in range(1,len(dots)):
        if dots[i][0] == point_w:
            height = abs(dots[i][1] - point_h)
        elif dots[i][1] == point_h:
            width = abs(dots[i][0] - point_w)
    answer = height * width
    return answer