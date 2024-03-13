def solution(priorities, location):
    queue = list(zip(priorities, range(len(priorities))))
    count = 0
    
    while queue:
        process = queue.pop(0)
        if any(process[0] < q[0] for q in queue):
            queue.append(process)
        else:
            count += 1
            if process[1] == location:
                return count
