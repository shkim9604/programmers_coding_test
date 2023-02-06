def solution(my_string, num1, num2):
    answer = ''
    imsi = list(my_string)
    temp = imsi[num1]
    imsi[num1] = imsi[num2]
    imsi[num2] = temp
    answer = "".join(imsi)
    return answer