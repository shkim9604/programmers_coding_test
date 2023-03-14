def solution(dartResult):
    answer = 0
    num = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == "0" and dartResult[i - 1].isdigit():
                num[-1] = int("".join(str(num[-1]) + dartResult[i]))
            else:
                num.append(int(dartResult[i]))
        if dartResult[i] == "S":
            num[-1] = pow(num[-1], 1)
        elif dartResult[i] == "D":
            num[-1] = pow(num[-1], 2)
        elif dartResult[i] == "T":
            num[-1] = pow(num[-1], 3)
        elif dartResult[i] == "#":
            num[-1] = num[-1] * -1
        elif dartResult[i] == "*":
            if len(num) == 1:
                num[-1] = num[-1] * 2
            else:
                num[-1] = num[-1] * 2
                num[-2] = num[-2] * 2
    answer = sum(num)
    return answer
