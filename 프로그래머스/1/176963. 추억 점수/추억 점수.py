def solution(name, yearning, photo):
    people_dict = {}
    
    for n, y in zip(name, yearning):
        people_dict[n] = y
    # print(people_dict)
    
    result = []
    for i in photo:
        score = 0
        for j in i:
            score += people_dict.get(j, 0)
        result.append(score)
    # print(result)
    
    return result