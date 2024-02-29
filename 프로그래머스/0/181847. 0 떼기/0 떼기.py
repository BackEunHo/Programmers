def solution(n_str):
    answer = ''
    for idx in range(len(n_str)):
        if n_str[idx] == "0":
            continue
        else:
            return n_str[idx:]