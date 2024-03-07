def solution(order):
    result = 0
    for word in order:
        if "americano" in word:
            result += 4500
        elif "cafelatte" in word:
            result += 5000
        elif word == "anything":
            result += 4500
    return result
            