def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in range(len(arr)):
            arr[i] = arr[i] + [0] * abs(row - col)
    elif row < col:
        for _ in range(abs(row - col)):
            arr.append([0] * col)
    return arr
            
            
            
            