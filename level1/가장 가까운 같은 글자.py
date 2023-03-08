def solution(s):
    answer = []
    front = []
    for i in s:
        if i not in front:
            answer.append(-1)
            front.append(i)
        else:
            count = 0
            for j in front[-1::-1]:
                count += 1
                if j == i:
                    answer.append(count)
                    break
            front.append(i)
    return answer