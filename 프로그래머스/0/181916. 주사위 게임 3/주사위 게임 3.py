def solution(a, b, c, d):
    answer = 0
    arr_dice = [a,b,c,d] # [2, 5, 2, 6]
    set_dice = list(set(arr_dice)) # [2,5,6]
    dic_count = {}
    for i in range(len(set_dice)): 
        dic_count[set_dice[i]] = arr_dice.count(set_dice[i])  #{2: 2, 5: 1, 6:1}
        
    if len(set_dice) == 1:
        return 1111 * set_dice[0]
    elif len(set_dice) == 2:
        if dic_count[max(dic_count, key=dic_count.get)] == 3:
            p = max(dic_count, key=dic_count.get)
            q = min(dic_count, key=dic_count.get)
            return (10 * p + q)**2
        else:
            p = set_dice[0]
            q = set_dice[1]
            return (p + q) * abs(p - q)
    elif len(set_dice) == 3:
        temp = max(dic_count, key=dic_count.get)
        new_arr = [x for x in arr_dice if x != temp]
        return new_arr[0] * new_arr[1]
    else:
        return min(arr_dice)