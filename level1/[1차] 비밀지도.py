def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(arr1[i] | arr2[i])
    for i in range(n):
        var = bin(answer[i]).split("b")
        var = var[1].zfill(n).replace("1","#").replace("0"," ")
        answer[i] = var
    return answer