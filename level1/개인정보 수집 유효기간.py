def solution(today, terms, privacies):
    answer = []
    today = today.split(".")
    today_year, today_month, today_day = int(today[0]), int(today[1]), int(today[2])
    contract_term = {}
    for i in terms:
        i = i.split(" ")
        contract_term[i[0]] = int(i[1])
    for i in range(len(privacies)):
        date, condition = privacies[i].split(" ")
        pri_year, pri_month, pri_day = int(date[0:4]), int(date[5:7]), int(date[8:])
        pri_month += contract_term[condition]

        while pri_month > 12:
            pri_month -= 12
            pri_year += 1

        if pri_year > today_year:
            continue
        elif pri_year == today_year:
            if pri_month > today_month:
                continue
            elif pri_month == today_month:
                if pri_day > today_day:
                    continue
        answer.append(i + 1)
    return answer