def solution(arr, queries):
    for idx in range(len(queries)):
        temp = arr[queries[idx][0]]
        arr[queries[idx][0]] = arr[queries[idx][1]]
        arr[queries[idx][1]] = temp
    return arr
        
        
        