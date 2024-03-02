def solution(str_list, ex):
    to_remove = []
    for word in str_list:
        if ex in word:
            to_remove.append(word)
    
    for word in to_remove:
        str_list.remove(word)
    
    return ''.join(str_list)
