def solution(my_string):
    answer = ''
    no_string = ['a','e','i','o','u']
    for i in my_string:
        if i in no_string:
            answer += ''
        else:
            answer += i
    return answer