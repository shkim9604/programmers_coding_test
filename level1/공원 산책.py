def solution(park, routes):
    obstacle = []  # 장애물 좌표
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i, j]
            elif park[i][j] == 'X':
                a = [i, j]
                obstacle.append(a)

    w = len(park[0]) - 1  # 가로
    h = len(park) - 1  # 세로

    for i in routes:
        i = i.split()
        move_count = 0
        if i[0] == 'E':
            for j in range(int(i[1])):
                start[1] += 1
                move_count += 1
                if start in obstacle:
                    start[1] -= move_count
                    break
                if start[1] > w:
                    start[1] -= move_count
                    break
        elif i[0] == 'W':
            for j in range(int(i[1])):
                start[1] -= 1
                move_count += 1
                if start in obstacle:
                    start[1] += move_count
                    break
                if start[1] < 0:
                    start[1] += move_count
                    break
        elif i[0] == 'S':
            for j in range(int(i[1])):
                start[0] += 1
                move_count += 1
                if start in obstacle:
                    start[0] -= move_count
                    break
                if start[0] > h:
                    start[0] -= move_count
                    break
        elif i[0] == 'N':
            for j in range(int(i[1])):
                start[0] -= 1
                move_count += 1
                if start in obstacle:
                    start[0] += move_count
                    break
                if start[0] < 0:
                    start[0] += move_count
                    break

    return start