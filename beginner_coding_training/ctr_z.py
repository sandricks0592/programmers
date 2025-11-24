def solution(s):
    stack = []
    for i in s.split():
        if i == 'Z':
            if stack:
                stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)

s = "1 2 Z 3"
print(solution(s))


# 최신값을 뺄 떄는 stack 생각하기