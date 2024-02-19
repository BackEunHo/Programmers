def solution(binomial):
    result = 0
    operator = "+"
    binomial = binomial.split(" ")
    for item in binomial:
        if item.isdigit():
            if operator == "+":
                result += int(item)
            elif operator == "-":
                result -= int(item)
            elif operator == "*":
                result *= int(item)
        else:
            operator = item
    return result
                