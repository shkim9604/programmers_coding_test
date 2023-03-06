def solution(array, commands):
    answer = []
    reply = []
    for i in range(len(commands)):
        reply = array[commands[i][0] - 1:commands[i][1]]
        reply.sort()
        answer.append(reply[commands[i][2] - 1])

    return answer