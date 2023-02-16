def solution(num, total):
    answer = []
    start_num = 0
    for i in range(1,num):
        start_num += i
    start_num = (total-start_num) // num
    for i in range(start_num,start_num+num):
        answer.append(i)
    return answer