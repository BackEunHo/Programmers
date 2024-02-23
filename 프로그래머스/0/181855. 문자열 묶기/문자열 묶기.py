def solution(strArr):
    # 각 문자열의 길이를 기준으로 그룹화
    groups = {}
    max_group_size = 0
    for s in strArr:
        length = len(s)
        if length not in groups:
            groups[length] = 1
        else:
            groups[length] += 1
        max_group_size = max(max_group_size, groups[length])
    
    return max_group_size
