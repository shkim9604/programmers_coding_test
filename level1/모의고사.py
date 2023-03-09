def solution(answers):
    answer = []
    # 수포자1,2,3 찍는 방식
    first = "12345"
    second = "21232425"
    third = "3311224455"
    # 수포자 맞은문제 카운트
    first_count = 0
    second_count = 0
    third_count = 0
    # 수포자와 맞은문제 딕셔너리로 저장
    count = {}
    for i in range(len(answers)):
        if answers[i] == int(first[i % len(first)]):
            first_count += 1
        if answers[i] == int(second[i % len(second)]):
            second_count += 1
        if answers[i] == int(third[i % len(third)]):
            third_count += 1
    count[1] = first_count
    count[2] = second_count
    count[3] = third_count
    #수포자 많이 맞은개수
    max_count = max(count.values())
    for k,v in count.items():
        if v == max_count:
            answer.append(k)
    return answer