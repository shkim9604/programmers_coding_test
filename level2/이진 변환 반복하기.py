def solution(s):
    answer = []
    count = 0
    switch = 0
    while s != '1':
        count += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        switch += 1
    answer.append(switch)
    answer.append(count)
    return answer