def solution(lottos, win_nums):
    answer = []
    win_logic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    match_count = 0 #처음에 맞춘번호 개수
    plus = 0 # 0의 개수
    for i in lottos:
        if i in win_nums:
            match_count += 1
        if i == 0:
            plus += 1
    max_count = match_count + plus
    # match_count 최저 max_count는 최고
    answer.append(win_logic[max_count])
    answer.append(win_logic[match_count])
    return answer