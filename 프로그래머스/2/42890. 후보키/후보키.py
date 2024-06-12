import itertools

def solution(relation):
    col_num = len(relation[0])
    people_num = len(relation)
    minimality = []
    no_minimal = set()

    test_cases = [[k] for k in range(col_num)]
    
    for i in range(2, people_num + 1):
        for j in itertools.combinations(range(col_num), i):
            test_cases.append(list(j))
    
    for test_case in test_cases:
        temp_set = set()
        for l in range(people_num):
            temp_len = ""
            for m in test_case:
                temp_len += relation[l][m]
            temp_set.add(temp_len)
        if len(temp_set) == people_num:
            minimality.append(set(test_case))
    print(minimality)
    
    for n in minimality:
        for o in minimality:
            if n != o and n.issubset(o) and n not in no_minimal:
                no_minimal.add(tuple(o))
    print(no_minimal)

    return len(minimality) - len(no_minimal)