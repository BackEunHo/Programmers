def solution(s):
    result = 0
    s = list(s.split(' '))
    for idx in range(len(s)):
        if s[idx] == 'Z':
            result -= int(s[idx - 1])
        else:
            result += int(s[idx])
    return result
                
    
        