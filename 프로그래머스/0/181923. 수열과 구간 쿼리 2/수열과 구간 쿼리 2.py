def solution(arr, queries):
    answer = []
    for query in queries:
        temp_arr = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                temp_arr.append(arr[i])
        try:
            answer.append(min(temp_arr))
        except:
            answer.append(-1)
    return answer
