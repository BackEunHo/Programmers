result = [char for char in input()]
for i in range(len(result)):
    if result[i].isupper() == True:
        print(result[i].lower(), end='')
    else:
        print(result[i].upper(), end='')
