def solution(arr, intervals):
    answer = []
    for interval in intervals:
        for i in arr[interval[0]:interval[1]+1]:
            answer.append(i)    
    return answer