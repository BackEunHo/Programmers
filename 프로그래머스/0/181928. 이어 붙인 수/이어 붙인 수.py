def solution(num_list):
    even = ''
    odd = ''
    for idx in num_list:
        if idx % 2 == 0:
            even += str(idx)
        else:
            odd += str(idx)
    return int(even) + int(odd)
            