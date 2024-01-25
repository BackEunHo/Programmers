def solution(num_list):
    multi = 1
    for x in num_list:
        multi *= x
    power = sum(x for x in num_list)**2
    return 1 if power > multi else 0