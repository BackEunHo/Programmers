def solution(rank, attendance):
    answer = 0
    cnt = 0
    for idx in range(1,len(rank)+1):
        n = rank.index(idx)
        if attendance[n] == True:
            answer += n * 100**(2 - cnt)
            cnt += 1
        if cnt == 3:
            break
    return answer