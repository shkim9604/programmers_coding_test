def solution(before, after):
    answer = 0
    b_dic = dict()
    a_dic = dict()
    b_set = list(set(before))
    a_set = list(set(after))
    b_set.sort()
    a_set.sort()
    for i in b_set:
        b_dic[i] = before.count(i)
    for i in a_set:
        a_dic[i] = after.count(i)
    if b_dic == a_dic:
        answer = 1
    return answer