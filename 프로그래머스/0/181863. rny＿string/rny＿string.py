def solution(rny_string):
    rny_string = list(rny_string)
    for idx in range(len(rny_string)):
        if rny_string[idx] == "m":
            rny_string[idx] = "rn"
    return ''.join(rny_string)
            
        
        