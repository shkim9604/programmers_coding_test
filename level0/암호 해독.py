def solution(cipher, code):
    answer = ''
    cipher = cipher[code-1:]
    for i in range(0,len(cipher),code):
        answer += cipher[i]
    return answer