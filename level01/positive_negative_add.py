def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
    return answer

absolutes = [4,7,12]
signs = [true, false, true]
print(solution(absolutes, signs))

#  true 랑 false는 생략으로 표현해보자.