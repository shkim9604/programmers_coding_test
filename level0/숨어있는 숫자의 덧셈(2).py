def solution(my_string):
    answer = 0
    num_place = ""
    for i in my_string:
        try:
            a = int(i)
            num_place += i
        except:
            if num_place == "":
                continue
            answer += int(num_place)
            num_place = ""
    if num_place != "":
        answer += int(num_place)
    return answer