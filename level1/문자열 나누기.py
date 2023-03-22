def solution(s):
    answer = 0
    first_count = 0 #첫문자 나온횟수
    another_count = 0 #그이외 나온숫자 횟수
    first_str = "" #첫문자 저장
    for i in s:
        if first_str == "": #first_str이 비어있으면 문자열 분리를 의미
            first_str = i
            first_count += 1
        else:
            if first_str == i: #첫문자와 같은문자이면 첫문자 나온횟수 count +
                first_count += 1
            else:
                another_count += 1 #첫문자와 같지않으면 다른문자 나온횟수 count +
            if first_count == another_count:#나온횟수가 같다면 answer에 + 나온횟수 초기화
                answer += 1
                first_count = 0
                another_count = 0
                first_str = ""
    if first_str != "": #마지막글자가 남아있을수있으므로 최종확인
        answer += 1
    return answer