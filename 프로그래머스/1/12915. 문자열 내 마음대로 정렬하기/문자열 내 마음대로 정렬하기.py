def solution(strings, n):
    strings = sorted(strings, key = lambda x:x, reverse = False)
    strings = sorted(strings, key = lambda x:x[n], reverse = False)
    # print(strings)
    return strings