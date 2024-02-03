def solution(n):
    divisors = []
    for i in range(1,int(n**2) + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)