def solution(numbers, hand):
    answer = ''
    hand_loc = {}
    count = 0
    for i in range(1,4):
        for j in range(1,4):
            a = []
            a.append(i)
            a.append(j)
            count += 1
            hand_loc[count] = a
    hand_loc[0] = [4, 2]
    left_loc = [4,1] # *
    right_loc = [4,3] # #
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left_loc = hand_loc[i]
        elif i in [3, 6, 9]:
            answer += "R"
            right_loc = hand_loc[i]
        elif i in [2, 5, 8, 0]:
            pad = hand_loc[i]
            if abs(pad[0] - left_loc[0]) + abs(pad[1] - left_loc[1]) < abs(pad[0] - right_loc[0]) + abs(pad[1] - right_loc[1]):
                answer += "L"
                left_loc = pad
            elif abs(pad[0] - left_loc[0]) + abs(pad[1] - left_loc[1]) == abs(pad[0] - right_loc[0]) + abs(pad[1] - right_loc[1]):
                if hand == "right":
                    answer += "R"
                    right_loc = pad
                else:
                    answer += "L"
                    left_loc = pad
            else:
                answer += "R"
                right_loc = pad
    return answer