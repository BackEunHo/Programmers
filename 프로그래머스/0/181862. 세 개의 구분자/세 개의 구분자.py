def solution(myStr):
    if set(myStr) == {'a','b','c'}:
        return ["EMPTY"]
    myStr = myStr.replace('a',' ')
    myStr = myStr.replace('b',' ')
    myStr = myStr.replace('c',' ')
    myStr = myStr.split()
    return myStr