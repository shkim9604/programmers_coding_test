def solution(babbling):
    answer = 0
    talking = ["aya","ye","woo","ma"]
    for i in babbling:
        for j in talking:
            if j in i:
                i = i.replace(j,"!",1)
        if i.replace("!","") == "":
            answer += 1
    return answer