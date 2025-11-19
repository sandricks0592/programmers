# def solution(numlist, n):
#     answer = []
#     diff = []
#     for i in numlist:
#         diff.append(abs(i-n))
#     answer = sorted(diff)
#     return answer

def solution(numlist, n):
    answer = []
    nums = numlist[:]
    while nums:
        best = nums[0]
        for i in nums:
            # i가 best보다 n과 더 가깝다면 i를 선택
            if abs(i - n) < abs(best - n):
                best = i

            # 거리가 같으면 더 큰 숫자를 선택해야 함
            elif abs(i - n) == abs(best - n) and i > best:
                best = i
        answer.append(best)
        nums.remove(best)

    return answer

numlist = [1, 2, 3, 4, 6, 5]
n = 4
print(solution(numlist, n))

#  while로 nums에 남아있는게 없을때까지 전체를 반복
# best = nums[0] 하나를 지정해 후보로 지정
