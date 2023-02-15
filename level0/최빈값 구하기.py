def solution(array):
    answer = 0
    count= []
    a = {}
    a_reverse = {}
    array_set = set(array)
    for i in array_set:
        count.append(array.count(i))
        a[i] = array.count(i)
    x = max(count)
    if count.count(x) > 1:
        answer = -1
    else:
        for k,v in a.items():
            a_reverse[v] = k
        answer = a_reverse[x]
    return answer