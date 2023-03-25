def solution(survey, choices):
    answer = ''
    index = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for a, b in zip(choices, survey):
        count = 3
        if a in [1, 2, 3]:
            index[b[0]] += (count - (a - 1))
        elif a in [5, 6, 7]:
            index[b[1]] += (count + (a - 7))
        else:
            continue
    key = list(iter(index))
    for i in range(0, len(index), 2):
        if index[key[i]] > index[key[i + 1]] or index[key[i]] == index[key[i + 1]]:
            answer += key[i]
        elif index[key[i]] < index[key[i + 1]]:
            answer += key[i + 1]

    return answer