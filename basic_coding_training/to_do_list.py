def solution(todo_list, finished):
    answer = []
    for v,k in zip(todo_list,finished):
        if k == False:
            answer.append(v)
    return answer

todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]
print(solution(todo_list, finished))