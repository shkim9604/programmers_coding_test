def solution(numlist, n):
    answer = []
    distance = {}
    for i in numlist:
        distance[i] = abs(n - i)
    num_min = min(distance.values())
    num_max = max(distance.values())
    for i in range(num_min, num_max + 1):
        save = []
        for j in numlist:
            if i == distance[j]:
                save.append(j)
        save.sort(reverse=True)
        for a in save:
            answer.append(a)
    return answer