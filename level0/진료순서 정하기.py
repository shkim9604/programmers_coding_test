def solution(emergency):
    answer = []
    result = sorted(emergency,reverse=True) # 응급도 높은순서로 정렬
    order = {} # 응급도순위와 진료순서 를 매칭
    for i in range(1,len(emergency)+1):
        order[result[i-1]] = i
    for i in emergency:
        answer.append(order[i])
    return answer