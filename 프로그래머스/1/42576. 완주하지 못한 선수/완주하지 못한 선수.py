from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    result = participant - completion
    answer = list(result.keys())[0]
    return answer