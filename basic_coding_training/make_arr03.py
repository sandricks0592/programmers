# def solution(arr, intervals):
#     answer = []
#     for a,b in zip(intervals):
#         answer = intervals[a[0]:a[1]+1]+intervals[b[0]:b[1]+1]
#     return answer

def solution(arr, intervals):
    answer = []
    first_start,first_end = intervals[0]
    first_slice = arr[first_start:first_end+1]

    second_start,second_end = intervals[1]
    second_slice = arr[second_start:second_end+1]

    answer = first_slice + second_slice

    return answer

arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]
print(solution(arr, intervals))