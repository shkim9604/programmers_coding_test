def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    string = ''
    for i in range(1,len(my_string),2):
        if my_string[i] == "+":
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    return answer