def solution(my_string, indices):
    my_string = list(my_string)
    indices.sort(reverse=True)
    for idx in indices: del my_string[idx]
    return ''.join(my_string)