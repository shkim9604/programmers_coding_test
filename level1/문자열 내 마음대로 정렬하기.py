def solution(strings, n):
    answer = []
    sort_char = []
    temp = []
    for i in strings:
        sort_char.append(i[n])
    sort_char.sort()
    imsi_str = list(set(sort_char))

    for i in range(len(imsi_str)):
        if sort_char.count(imsi_str[i]) >= 2:
            for j in strings:
                if imsi_str[i] == j[n]:
                    temp.append(j)
    temp.sort()
    for i in strings:
        if i not in temp:
            temp.append(i)
    for i in sort_char:
        for j in temp:
            if j[n] == i:
                answer.append(j)
                temp.remove(j)
                break
    return answer