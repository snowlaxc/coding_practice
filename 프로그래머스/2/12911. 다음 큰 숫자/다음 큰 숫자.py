def solution(n):
    bin_n = bin(n)[2:]
    count = bin_n.count("1")
    
    for i in range(n+1, 1000000):
        if bin(i)[2:].count("1") == count:
            return i