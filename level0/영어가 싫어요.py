def solution(numbers):
    answer = ""
    number_switch = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    num_string = ""
    for i in numbers:
        if num_string in number_switch:
            answer += str(number_switch[num_string])
            num_string = ""
            num_string += i
        else:
            num_string += i
    if num_string in number_switch:
        answer += str(number_switch[num_string])
    return int(answer)