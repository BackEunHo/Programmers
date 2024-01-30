
def solution(n, answer = None):
    if answer == None:
        answer = []
    answer.append(n)
    
    if n == 1:
        return answer
    elif n % 2 == 0:
        return solution(n // 2,answer)
    else:
        return solution(3 * n + 1 , answer)
