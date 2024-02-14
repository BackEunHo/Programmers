def solution(arr):
    temp = arr.copy()  # 원본 리스트를 복사하여 temp에 저장
    cnt = 0
    for i in range(len(arr)):
        num = arr[i]
        if num >= 50 and num % 2 == 0:
            arr[i] = num // 2
        elif num < 50 and num % 2 != 0:
            arr[i] = num * 2 + 1
    if temp == arr:
        return cnt
    else:
        cnt += 1
        return cnt + solution(arr)  # 반환 값을 이용하여 cnt 값을 누적시킴