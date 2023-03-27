def solution(s, skip, index):
    answer = ''
    for i in s:
        count = 0
        while count != index:
            i = chr(ord(i) + 1)
            if ord(i) > 122:
                i = chr(ord(i) - 26)
            if i in skip:
                continue
            count += 1
        answer += i
    return answer