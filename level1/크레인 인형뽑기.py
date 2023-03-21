def solution(board, moves):
    answer = 0
    catch = []
    for i in moves:
        for j in range(len(board[i - 1])):
            if board[j][i - 1] != 0:
                catch.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(catch) >= 2 and catch[-1] == catch[-2]:
            answer += 2
            catch.pop()
            catch.pop()

    return answer
