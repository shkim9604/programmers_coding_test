def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz[i] = quiz[i].split('=')
    for i in quiz:
        num = eval(i[0])
        if num == int(i[-1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer