def solution(num_list):
    total_sum = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            total_sum *= num 
        return total_sum