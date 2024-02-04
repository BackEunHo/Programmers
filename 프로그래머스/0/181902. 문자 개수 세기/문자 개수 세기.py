def solution(my_string):
    answer = [0] * 52
    my_string = list(my_string)
    for i in my_string:
        if i.isupper():
            answer[ord(i) - 65] += 1
        else:
            answer[ord(i) - 71] += 1
    return answer
#A~Z: idx 0~25, ord(A): 65, ord(Z):90
#a~z: idx 26~52, ord(a): 97, ord(z): 122