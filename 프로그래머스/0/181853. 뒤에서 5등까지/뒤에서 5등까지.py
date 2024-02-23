def solution(num_list):
    result = []
    num_list.sort()
    for i in range(5):
        result.append(num_list[i])
    return result