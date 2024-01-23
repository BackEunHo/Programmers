def solution(code):
    answer = ''
    code = list(code)
    mode = 0
    for idx in range(0, len(code)):
        if code[idx]  == "1": mode = 1 - mode
        elif idx % 2 == mode: answer += code[idx]
    return 'EMPTY' if answer == '' else answer