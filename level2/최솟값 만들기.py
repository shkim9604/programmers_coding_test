def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[0] * B[-1]
        A.remove(A[0])
        B.pop()

    return answer