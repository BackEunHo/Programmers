def solution(numLog):
    result = ''
    for idx in range(1,len(numLog)):
        if numLog[idx] - numLog[idx - 1] == 1:
            result += "w"
        elif numLog[idx] - numLog[idx - 1] == -1:
            result += "s"
        elif numLog[idx] - numLog[idx - 1] == 10:
            result += "d"
        else:
            result += "a"
    return result
        