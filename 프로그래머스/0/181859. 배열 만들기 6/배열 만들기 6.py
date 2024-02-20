def solution(arr):
    stack = []
    for num in arr:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    return stack if stack else [-1]