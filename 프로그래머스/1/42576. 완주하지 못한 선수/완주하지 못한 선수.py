def solution(participant, completion):
    dict1 = {i:0 for i in participant}
    dict2 = {i:0 for i in participant}
    for i in participant:
        dict1[i] += 1
    for i in completion:
        dict2[i] += 1
    for i in dict1:
        if dict1[i] - dict2[i] == 1:
            return i
    
        