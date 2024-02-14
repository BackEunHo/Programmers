def solution(myString):
    myString = myString.lower()
    myString = [char.upper() if char == 'a' else char for char in myString]
    return ''.join(myString)