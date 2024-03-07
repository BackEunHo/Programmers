def solution(picture, k):
    result = []
    for row in picture:
        enlarged_row = ''.join([char * k for char in row])
        for _ in range(k):
            result.append(enlarged_row)
    return result