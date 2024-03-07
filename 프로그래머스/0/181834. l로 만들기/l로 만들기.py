def solution(myString):
    lst = list(myString)
    for idx in range(len(lst)):
        if ord(lst[idx]) < 108:
            lst[idx] = 'l'
    return ''.join(lst)
        
