def solution(my_string):
    answer = ''
    my_string =list(my_string.lower())
    my_string.sort()
    for i in my_string:
        answer += i
    return answer