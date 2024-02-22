def solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    if arr1_len > arr2_len:
        return 1 
    elif arr1_len < arr2_len:
        return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0

