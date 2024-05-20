import string

def solution(s, skip, index):
    alphabet = {}
    skip = list(skip)
    
    idx = 0
    for i in string.ascii_lowercase:
        if i not in skip:
            idx += 1
            alphabet[i] = idx
    alpha_len = len(alphabet)
    alpha_list = list(alphabet.keys())
    # print(alphabet)
    # print(alpha_list)
    
    answer = ''
    for j in s:
        new = alphabet[j] + index
        while new > alpha_len:
            new -= alpha_len
        # print(new)
        answer += alpha_list[new - 1]
    
    return answer