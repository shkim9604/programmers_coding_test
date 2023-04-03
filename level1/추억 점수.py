def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for i in photo:
        hap = 0
        for j in i:
            try:
                hap += score[j]
            except:
                continue
        answer.append(hap)
    return answer