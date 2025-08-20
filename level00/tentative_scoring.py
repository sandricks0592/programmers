# 성적 문의 학생들 번호 정수 list : numbers
# 가채점 문의 학생들 순서 list : our_score
# 실제 성적이 번호 순서대로 담긴 정수 list : score_list

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:  
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer
