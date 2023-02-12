def solution(keyinput, board):
    answer = [0, 0]
    max_width = board[0] // 2
    max_height = board[1] // 2
    for i in keyinput:
        if i == "left":
            if answer[0] - 1 < -max_width:
                continue
            else:
                answer[0] -= 1
        if i == "right":
            if answer[0] + 1 > max_width:
                continue
            else:
                answer[0] += 1
        if i == "up":
            if answer[1] + 1 > max_height:
                continue
            else:
                answer[1] += 1
        if i == "down":
            if answer[1] - 1 < -max_height:
                continue
            else:
                answer[1] -= 1

    return answer