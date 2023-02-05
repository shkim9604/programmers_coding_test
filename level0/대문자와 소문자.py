def solution(my_string):
    answer = ''
    string_up = my_string.upper()
    for i in range(len(my_string)):
        if my_string[i] == string_up[i]:
            answer += my_string[i].lower()
        else:
            answer += my_string[i].upper()
    return answer