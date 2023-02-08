def solution(array, n):
    answer = 0
    array.sort()
    min_num = 100
    for i in array:
        test = abs(n - i)
        if test < min_num:
            min_num = test
            answer = i

    return answer