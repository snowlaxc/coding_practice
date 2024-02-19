from collections import deque

def solution(sizes):
    width = []
    height = []
    for a, b in sizes:
        width.append(max(a, b))
        height.append(min(a, b))
        
    return max(width) * max(height)