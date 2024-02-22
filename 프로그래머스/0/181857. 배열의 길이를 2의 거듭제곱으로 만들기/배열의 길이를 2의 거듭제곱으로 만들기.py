def solution(arr):
    n = len(arr)
    target_length = 1
    while target_length < n:
        target_length *= 2
    num_zeros = target_length - n
    new_arr = arr + [0] * num_zeros
    return new_arr