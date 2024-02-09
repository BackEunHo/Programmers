def solution(arr):
    answer = []
    if arr.count(2) == 0: return [-1]
    elif arr.count(2) == 1: return [2]
    else: 
        indices = [idx for idx, val in enumerate(arr) if val == 2]
        return arr[indices[0]:indices[-1]+1]
    return answer