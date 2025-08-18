# 땅따먹기 게임의 땅(land)은 총 N행 4열

def solution(land):
    n = len(land)
    
    # 첫 번째 행은 그대로 시작
    dp = land[0]
    
    # 두 번째 행부터 마지막 행까지 반복
    for i in range(1, n):
        new_dp = [0]*4
        for j in range(4):
            # 같은 열 제외하고 위 행에서 최대값 선택
            new_dp[j] = land[i][j] + max(dp[k] for k in range(4) if k != j)
        dp = new_dp  # DP 갱신
    
    answer = max(dp)  # 마지막 행에서 최댓값 반환
    return answer
