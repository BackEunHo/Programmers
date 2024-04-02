def solution(array, commands):
    result = []
    for arr in commands:
        result.append(sorted(array[arr[0]-1:arr[1]])[arr[2]-1])
    return result