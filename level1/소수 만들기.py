def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):  # 0
        for j in range(i + 1, len(nums) - 1):  # 1
            for a in range(j + 1, len(nums)):
                prime = True
                hap = nums[i] + nums[j] + nums[a]
                for x in range(2, hap - 1):
                    if hap % x == 0:
                        prime = False
                        break
                if prime:
                    answer += 1
    return answer
