def solution(myString, pat):
    longest_substring = ''
    index = myString.find(pat)
    while index != -1:
        substring = myString[:index + len(pat)]
        if len(substring) > len(longest_substring):
            longest_substring = substring
        index = myString.find(pat, index + 1)
    return longest_substring