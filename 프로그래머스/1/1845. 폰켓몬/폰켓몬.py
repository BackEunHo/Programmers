def solution(nums):
    arr = list(set(nums))
    if len(arr) > (len(nums) // 2):
        return len(nums) // 2
    else:
        return len(arr)