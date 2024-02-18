def solution(myString):
    arr = myString.split("x")
    result = []
    for word in arr:
        result.append(len(word))
    return result