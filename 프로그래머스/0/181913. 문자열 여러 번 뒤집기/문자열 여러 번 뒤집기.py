def solution(my_string, queries):
    arr = list(my_string)
    for i in range(len(queries)):
        temp = arr[queries[i][0]:queries[i][1]]
        arr[queries[i][0]:queries[i][1]] = arr[queries[i][1]:queries[i][0]:-1]
        arr[queries[i][1]:queries[i][0]:-1] = temp
    return ''.join(arr)