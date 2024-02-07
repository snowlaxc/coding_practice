from collections import Counter

def solution(nums):
    nums_count = Counter(nums)
    answer = min(int(len(nums)/2), len(nums_count.keys()))
    return answer