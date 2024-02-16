def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    duplication = []
    for i in lost:
        if i in reserve:
            duplication.append(i)
    
    for j in duplication:
        lost.remove(j)
        reserve.remove(j)
    
    student = [1] * n
    
    for k in reserve:
        student[k-1] += 1
        
    for l in lost:
        student[l-1] -= 1
        
    for m in reserve:
        if m == 1:
            if student[m] == 0:
                student[m] += 1
                student[m-1] -= 1
                
        elif m != 1 and m != n:
            if student[m-2] == 0:
                student[m-2] += 1
                student[m-1] -= 1
            elif student[m] == 0:
                student[m] += 1
                student[m-1] -= 1

        elif m == n:
            if student[m-2] == 0:
                student[m-2] += 1
                student[m-1] -= 1
            
    return sum(list(min(o, 1) for o in student))