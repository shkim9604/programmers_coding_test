def solution(A, B):
    answer = -1
    a = list(A)
    b = list(B)
    count = 0
    for i in range(len(a)):
        if a == b:
            answer = count
            break
        temp = a[-1]
        for j in range(len(a)-2,-1,-1):
            a[j+1] = a[j]
        a[0] = temp
        count += 1
        if a == b:
            answer = count
            break
    return answer