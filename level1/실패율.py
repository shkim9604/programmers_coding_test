def solution(N, stages):
    answer = []
    rate = {}
    attender = len(stages)
    for i in range(1, N+1):
        a = stages.count(i)
        try:
            rate[i] = a/attender
            attender -= a
        except ZeroDivisionError:
            rate[i] = 0
    new_rate = sorted(rate.items(), key=lambda x: x[1] ,reverse=True)
    for i in new_rate:
        answer.append(i[0])
    return answer