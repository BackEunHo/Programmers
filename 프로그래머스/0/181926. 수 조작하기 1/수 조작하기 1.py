def solution(n, control):
    for idx in control:
        if idx == "w":
            n += 1
        elif idx == "s":
            n -= 1
        elif idx == "d":
            n += 10
        else:
            n -= 10
    return n