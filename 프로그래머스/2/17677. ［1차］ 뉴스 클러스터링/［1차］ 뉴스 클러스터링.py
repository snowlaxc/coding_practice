import string
from collections import Counter

def solution(str1, str2):
    uppercase = string.ascii_uppercase
    str1 = str1.upper()
    str2 = str2.upper()
    two_str1 = []
    two_str2 = []
    
    for i in range(1, len(str1)):
        if str1[i-1] in uppercase and str1[i] in uppercase:
            two_str1.append(str1[i-1]+str1[i])
        
    for j in range(1, len(str2)):
        if str2[j-1] in uppercase and str2[j] in uppercase:
            two_str2.append(str2[j-1]+str2[j])
            
    two_str1 = Counter(two_str1)
    two_str2 = Counter(two_str2)
    inter = list((two_str1 & two_str2).elements())    # Counter 숫자만큼 요소 반환
    union = list((two_str1 | two_str2).elements())

    print(two_str1, two_str2)
    print(inter, union)
        
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)