import itertools

def solution(orders, course):
    answer = []
    
    for c in course:
        course_dict = {}
        
        for order in orders:
            if len(order) >= c:
                order = list(order)
                for i in itertools.combinations(order, c):
                    i = tuple(sorted(i))
                    course_dict[i] = course_dict.get(i, 0) + 1
                    
        for k, v in course_dict.items():
            if (v == max(course_dict.values())) and (v > 1):
                answer.append(''.join(k))

    return sorted(answer)