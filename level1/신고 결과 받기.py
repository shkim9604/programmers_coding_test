def solution(id_list, report, k):
    answer = []
    report_list = {} # 누가 누구를 신고했는지
    report_count = {} # 아이디당 신고당항 횟수
    for i in id_list:
        report_list[i] = []
        report_count[i] = 0
    for i in report:
        i = i.split(" ")
        if i[1] not in report_list[i[0]]: #신고는 한번만 되기때문에 신고리스트에 없을때만 추가
            report_list[i[0]].append(i[1])
            report_count[i[1]] += 1
    for i in report_list:
        count = 0
        for j in report_list[i]:
            if report_count[j] >= k:
                count += 1
        answer.append(count)
    return answer