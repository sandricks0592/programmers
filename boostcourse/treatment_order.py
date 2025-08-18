def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)  # 응급도 높은 순 정렬
    for e in emergency:
        answer.append(sorted_emergency.index(e) + 1)  # 순위는 1부터 시작
    return answer
