def solution(my_string, index_list):
    answer = ''
    my_string = list(my_string)
    for i in range(len(index_list)):
        answer += my_string[index_list[i]]
    return answer 