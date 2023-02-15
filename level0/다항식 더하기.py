def solution(polynomial):
    answer = ''
    num_sum = [0,0]
    for i in polynomial.split():
        if i == 'x':
            num_sum[0] += 1
        elif i == '+':
            continue
        elif 'x' in i:
            num_sum[0] += int(i[:-1])
        else:
            num_sum[1] += int(i)
    if not num_sum[0] == 0:
        if num_sum[0] == 1:
            answer += 'x'
        else:
            answer += str(num_sum[0]) + "x"
    if not num_sum[1] == 0:
        if not answer == '':
            answer += ' + '
        answer += str(num_sum[1])
    return answer