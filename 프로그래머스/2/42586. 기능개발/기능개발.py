import math
def solution(progresses, speeds):
    progresses = [100 - i for i in progresses] #[7, 70, 45]
    temp = []
    for i in range(len(progresses)):
        temp.append(math.ceil(progresses[i] / speeds[i]))
    # temp = [7,3,9], [5,10,1,1,20,1]
    for j in range(1,len(temp)):
        if temp[j-1] > temp[j]:
            temp[j] = temp[j-1]
    # temp = [7,7,9], [5,10,10,10,20,20]
    return count_elements(temp)

def count_elements(arr):
    count_dict = {}
    for element in arr:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return list(count_dict.values())


