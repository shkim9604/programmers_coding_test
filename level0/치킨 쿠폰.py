def solution(chicken):
    answer = -1
    coupon = chicken
    service_chicken = 0
    rest = 1
    while coupon // 10 != 0:
        service_chicken += coupon // 10
        rest = coupon % 10
        coupon = coupon // 10 + rest
    answer = service_chicken
    return answer