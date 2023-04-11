def solution(players, callings):
    answer = []
    player_grade = {}  # 선수:등수
    grade_player = {}  # 등수:선수
    for i in range(len(players)):
        player_grade[players[i]] = i
        grade_player[i] = players[i]
    for i in callings:
        cur_loc = player_grade[i]  # 현재등수
        pre_loc = cur_loc - 1  # 이전등수
        pre_player = grade_player[pre_loc]  # 이전등수의 선수이름

        player_grade[i] = pre_loc
        player_grade[pre_player] = cur_loc

        grade_player[pre_loc] = i
        grade_player[cur_loc] = pre_player

    answer = list(grade_player.values())

    return answer