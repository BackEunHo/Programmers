def solution(myString):
    myString = myString.split("x")
    filtered_list = [x for x in myString if x != ""]
    filtered_list.sort()
    return filtered_list