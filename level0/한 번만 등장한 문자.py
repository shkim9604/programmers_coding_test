def solution(s):
    answer = ''
    s_dic = dict()
    s = sorted(s)
    for i in s:
        if i in s_dic.keys():
            s_dic[i] += 1
        else:
            s_dic[i] = 1
    for i in s_dic:
        if s_dic[i] == 1:
            answer += i
    return answer