def solution(numer1, denom1, numer2, denom2):
    answer = []
    h1 = numer1 * denom2 + numer2 * denom1
    h2 = denom1 * denom2
    num = 1
    for i in range(h1,0,-1):
        if h1 % i == 0 and h2 % i == 0:
            answer.append(int(h1 / i))
            answer.append(int(h2 / i))
            break
    return answer