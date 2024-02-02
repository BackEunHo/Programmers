
def solution(intStrs, k, s, l):
    return [int(number[s:s+l]) for number in intStrs if int(number[s:s+l]) > k]