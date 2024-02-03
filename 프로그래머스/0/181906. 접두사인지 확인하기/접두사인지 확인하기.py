def solution(my_string, is_prefix):
    arr_prefix = []
    for i in range(len(my_string)): arr_prefix.append(my_string[0:i+1])
    return 1 if is_prefix in arr_prefix else 0

    
    