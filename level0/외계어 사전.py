def solution(spell, dic):
    answer = 2
    spell_dic = dict()
    for i in spell:
        spell_dic[i] = 0
    for i in dic:
        possible = True
        for j in i:
            if j in spell:
                spell_dic[j] += 1
        for a in spell_dic:
            if spell_dic[a] == 0:
                possible = False
                break
        if possible == True:
            break
        for a in spell_dic:
            spell_dic[a] = 0
    if possible == True:
        answer = 1
    else:
        answer = 2
    return answer