def solution(keymap, targets):
    answer = []
    for i in targets:
        hap = 0
        for j in i:
            count = []
            for a in range(len(keymap)):
                try:
                    count.append(keymap[a].index(j))
                except:
                    count.append(101)
            if min(count) == 101:
                hap = -1
                break
            else:
                hap += min(count) + 1
        answer.append(hap)
    return answer
