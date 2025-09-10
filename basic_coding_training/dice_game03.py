# def solution(a, b, c, d):
#     answer = 0
#     list01 = (a,b,c,d)
#     for i in range(lent(list01)):
#         if a == b == c == d:
#             answer = 1111 * a
#         elif list01.count(i) == 1:
#             if i <= 2:
#                 answer = ( 10 * list01[i] + list01[i+1])**2
#             else:
#                 answer = ( 10 * list01[i] + list01[i-1])**2
#         elif list01.count(i) == 2:

    # return answer

def solution(a, b, c, d):
    answer = 0
    dice = (a, b, c, d)
    counts = {}
    
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    if  len(counts) == 1:        # 다 같을 때
        answer = dice[0] * 1111
    
    elif 3 in counts.values():      # 하나만 다를 때
        for k,v in counts.items():
            if v == 3:
                p = k
            else:
                q = k
        answer = (10 * p + q) ** 2
    
    elif len(counts) == 2 and all(v == 2 for v in counts.values()): # 두개씩 다를 때
        p, q = counts.keys()
        answer = (p + q) * abs(p - q)
    
    # elif len(counts) == 3:
    #     for k,v in counts.items():
    #         if v == 2:
    #             p = k
    #         else:
    #             q,r = counts.keys
    #         answer = q * r
    elif 2 in counts.values():
        for k,v in counts.items():
            if v == 2:
                p = k
            else:
                if 'q' not in locals():
                    q = k
                else:
                    r = k
        answer =  q * r

    
    elif len(counts) == 4:
        answer = min(a,b,c,d)
    
    return answer

print(solution(2,2,2,2))

# dic 사용 익숙해지기 key값 value값 사용하는법 기억하기, 절댓값은 abs() , 지역 변수가 없을 경우는 not in local() 기억해보기