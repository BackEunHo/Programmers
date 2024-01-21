def solution(my_string, overwrite_string, s):
    answer = ''
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    j=s
    for i in range(0,len(overwrite_string)):
        my_string[s] = overwrite_string[s-j]
        s+=1
    return ''.join(my_string)

print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))
