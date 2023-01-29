def solution(num_list):
    answer = []
    count = 0
    for i in num_list:
        if i % 2 == 0:
            count += 1
    answer.append(count)
    answer.append(len(num_list)-count)
    return answer