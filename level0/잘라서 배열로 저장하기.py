def solution(my_str, n):
    answer = []
    while 1:
        if len(my_str) <= n:
            answer.append(my_str[:len(my_str)])
            break
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer