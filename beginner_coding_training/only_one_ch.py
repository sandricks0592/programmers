def solution(s):
    answer = ''
    result = ''
    for i in s:
        if s.count(i) == 1:
            result += i
    answer= "".join(sorted(result))
    return answer

s = "abcabcadc"
print(solution(s))

# join과 sorted를 좀 더 잘 사용해봐!!!