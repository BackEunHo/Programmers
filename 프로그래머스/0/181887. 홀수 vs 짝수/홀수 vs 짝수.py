def solution(num_list):
    even = 0
    odd = 0
    for idx,value in enumerate(num_list):
        idx += 1 
        if idx % 2 == 0:
            odd += value
        else:
            even += value
    return max(even,odd)
        