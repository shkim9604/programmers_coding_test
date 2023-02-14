def solution(score):
    answer = []
    sum_score = []
    for i in score:
        sum_score.append(sum(i))
    sort_sum = sorted(sum_score, reverse=True)
    for i in sum_score:
        if i == 0:
            answer.append(len(sort_sum))
            continue
        answer.append(sort_sum.index(i) + 1)
    return answer